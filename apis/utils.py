import requests
import pandas as pd
from pprint import pprint


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
        print("CATASTROPH ERROR ======================")
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


def get_general_response(df_data):
    df_data["value"] = df_data["px"] * df_data["qty"]
    orders = ("asks", "bids")
    response = {}
    for symbol in df_data["symbol"].unique():
        # total_orders = 0
        response[symbol] = {}
        for order in orders:
            df_focus = df_data[
                (df_data["order_type"] == order) & (df_data["symbol"] == symbol)
            ]
            response[symbol][order] = {}
            response[symbol][order]["count"] = str(df_focus["num"].count())
            response[symbol][order]["qty"] = str(df_focus["qty"].sum())
            response[symbol][order]["value"] = str(df_focus["value"].sum())
            # total_orders += df_focus['num'].count()
        # response[symbol]["total_order"] = str(total_orders)
    # response = {k: v for k, v in sorted(response.items(), key=lambda item: item[1]["total_order"])}
    pprint(response)
    return response
