"""Custom exceptions."""


class AfterShipException(Exception):
    """Base exception for AfterShip."""


class AfterShipCommunicationException(AfterShipException):
    """Communication exception for AfterShip."""
