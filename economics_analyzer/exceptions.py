"""Custom exceptions for application-level failures."""


class AppError(Exception):
    """Base application error."""


class DataSourceError(AppError):
    """Raised when input files cannot be read."""


class DataValidationError(AppError):
    """Raised when CSV row data cannot be parsed."""


class UnknownReportError(AppError):
    """Raised when requested report is not registered."""
