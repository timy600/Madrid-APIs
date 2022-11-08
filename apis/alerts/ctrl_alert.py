"""Alert Controller."""
from flask import Blueprint, request
from flask_restx import Api, Resource, fields, Namespace  # Api

from .dto import AlertDTO

api = AlertDTO.api


@api.route("/")
class Alerts(Resource):
    """Show a list of alerts or add a new one."""

    @api.doc(description="Retrieve Alert list.")
    @api.marshal_with(AlertDTO.listed_alerts, code=200)
    def get(self):
        """Fetch a list"""
        return {
            "message": "This endpoint should return a list of entities",
            "method": request.method,
        }

    @api.doc(description="Create an alert.")
    @api.expect(AlertDTO.model)
    @api.marshal_with(AlertDTO.listed_alerts, code=200)
    def post(self):
        """Create an alert"""
        return {
            "message": "This endpoint should create an entity",
            "method": request.method,
            "body": request.json,
        }


@api.route("/<alert_id>")
class AlertSingle(Resource):
    """Handle one alert."""

    @api.doc(description="Retrieve an alert.")
    @api.marshal_with(AlertDTO.listed_alerts, code=200)
    def get(self, alert_id):
        """Fetch a specific alert."""
        return {
            "message": "This endpoint should return a list of entities",
            "method": request.method,
        }

    @api.doc(description="Update an alert.")
    @api.expect(AlertDTO.model)
    @api.marshal_with(AlertDTO.listed_alerts, code=200)
    def patch(self, alert_id):
        """Update an alert."""
        return {
            "message": "This endpoint should return a list of entities",
            "method": request.method,
        }

    @api.doc(description="Delete an entry.")
    @api.marshal_with(AlertDTO.listed_alerts, code=200)
    def delete(self, alert_id):
        """Delete an item."""
        return {
            "message": "This endpoint should return a list of entities",
            "method": request.method,
        }
