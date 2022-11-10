"""Crypto DTO."""
from flask_restx import Namespace


class CryptoDTO:
    """Crypto DTO Class"""

    api = Namespace(
        "cryptocurrencies", description="blockchain.com API related endpoints"
    )
