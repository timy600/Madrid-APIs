from datetime import datetime

from flask import Blueprint, jsonify
from flask import render_template
from apis.models.config import df_to_sql

import requests
import pandas as pd
from pprint import pprint
from flask_restx import Resource

# extract_pages = Blueprint("extract_pages", __name__, template_folder="templates")

from .dto import CryptoDTO

api = CryptoDTO.api


def call_api(symbol: str, order=None):
    url_base = "https://api.blockchain.com/v3/exchange/l3/"
    url = url_base + symbol
    headers = {"accept": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        if order:
            data = response.json()[order]
            df = pd.DataFrame(data)
            return df
        else:
            data = response.json()
            return data
    except requests.exceptions.RequestException as e:
        print("REQUEST ERROR ======================")
        print(e)
        raise e


def get_order_response(df_data):
    df_data["value"] = df_data["px"] * df_data["qty"]

    response = {
        "average_value": str(df_data["value"].mean()),
        "greater_value": df_data.max().map(str).to_dict(),
        "lesser_value": df_data.min().map(str).to_dict(),
        "total_qty": str(df_data["qty"].sum()),
        "total_px": str(df_data["px"].sum()),
    }
    pprint(response)
    return response


@api.route("/data/<symbol>")
class CryptoCaller(Resource):
    """Interact with crypto.com API."""

    def get(self, symbol):
        try:
            data = call_api(symbol)
        except requests.exceptions.JSONDecodeError:
            return "Error JSON"

        api_call_datetime = datetime.now().replace(second=0, microsecond=0)
        df_bids = pd.DataFrame(data["bids"])
        df_bids["order_type"] = "bids"

        df_asks = pd.DataFrame(data["asks"])
        df_asks["order_type"] = "asks"

        df = pd.concat([df_bids, df_asks])
        df["order_date"] = api_call_datetime
        df["symbol"] = symbol
        df_to_sql(df)
        response = get_order_response(df)
        return jsonify(response)


@api.route("/current/<order>/<symbol>")
class CryptoCurrentCaller(Resource):
    """Current Data, no interaction with the Database."""

    def get(self, order, symbol):
        try:
            df = call_api(symbol, order)
        except requests.exceptions.JSONDecodeError:
            return "Error JSON"
        # print(df.describe())
        response = get_order_response(df)
        return jsonify(response)
