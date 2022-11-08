"""Alerts DTO."""
from flask_restx import Namespace, fields


class AlertDTO:
    """Alert DTO Class"""

    api = Namespace("alerts", description="Alerts related endpoints")

    model_fields = {
        "AlertName": fields.String,
        "AlertDescription": fields.String,
    }

    model = api.model(
        "Alert", {"msg": fields.String(required=True, description="The alert details")}
    )

    category = api.model(
        "Category",
        {"name": fields.String(required=True, description="The category name")},
    )

    listed_alerts = api.model(
        "ListedAlerts",
        {
            "id": fields.String(required=True, description="The Alert Id"),
            "category": fields.Nested(
                category, description="The Category of the alert"
            ),
            "alerts": fields.Nested(model, description="The Alerts"),
        },
    )

    data_resp = api.model(
        "Alert Response",
        {
            "message": fields.String,
            "status_code": fields.Integer,
            "data": fields.Nested(model),
        },
    )

    data_resp_list = api.clone(
        "Alerts Response",
        data_resp,
        {
            "data": fields.List(fields.Nested(model)),
        },
    )

    error_resp = api.model(
        "Alert Error Response",
        {"message": fields.String, "status_code": fields.Integer},
    )
