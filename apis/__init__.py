"""Package for apis code."""
from flask import Blueprint
from flask_restx import Api

from apis.alerts.ctrl_alert import api as api_alert
from apis.cryptos import api_exploit


api_bp = Blueprint("api", __name__)
api = Api(
    api_bp,
    title="Testing the multiple api in one swagger",
    version="0.0",
    description="API to test the swagger",
)

api.add_namespace(api_alert)
api.add_namespace(api_exploit)
