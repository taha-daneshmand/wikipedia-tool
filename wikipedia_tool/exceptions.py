"""
This module defines custom exceptions for the wikipedia_tool library.

These exceptions provide detailed error reporting for various error conditions
encountered within the library, including API errors, parsing errors, configuration
issues, network problems, and data processing failures.
"""


class WikipediaToolError(Exception):
    """
    Base exception class for errors raised by the wikipedia_tool library.

    All custom exceptions in the library should inherit from this class.
    """
    pass


class WikiAPIError(WikipediaToolError):
    """
    Exception raised when an error occurs during interaction with the Wikipedia API.

    Attributes:
        message (str): Description of the error.
        status_code (int, optional): HTTP status code returned by the API, if applicable.
        payload (dict, optional): Additional error data returned by the API.
    """
    def __init__(self, message: str, status_code: int = None, payload: dict = None) -> None:
        self.message = message
        self.status_code = status_code
        self.payload = payload
        super().__init__(message)

    def __str__(self) -> str:
        base = self.message
        if self.status_code is not None:
            base += f" (Status code: {self.status_code})"
        return base


class WikiParsingError(WikipediaToolError):
    """
    Exception raised when an error occurs during the parsing of Wikipedia content.

    Attributes:
        message (str): Description of the parsing error.
        raw_content (str, optional): The raw content that caused the parsing error.
    """
    def __init__(self, message: str, raw_content: str = None) -> None:
        self.message = message
        self.raw_content = raw_content
        super().__init__(message)

    def __str__(self) -> str:
        base = self.message
        if self.raw_content:
            base += " | Raw content excerpt: " + self.raw_content[:100]
        return base


class WikiConfigurationError(WikipediaToolError):
    """
    Exception raised for errors in the configuration of wikipedia_tool.

    Attributes:
        message (str): Explanation of the configuration error.
    """
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return self.message


class WikiNetworkError(WikipediaToolError):
    """
    Exception raised when a network-related error occurs during an API request.

    Attributes:
        message (str): Description of the network error.
        original_exception (Exception, optional): The underlying exception from the network library.
    """
    def __init__(self, message: str, original_exception: Exception = None) -> None:
        self.message = message
        self.original_exception = original_exception
        super().__init__(message)

    def __str__(self) -> str:
        base = self.message
        if self.original_exception:
            base += f" | Caused by: {repr(self.original_exception)}"
        return base


class WikiDataError(WikipediaToolError):
    """
    Exception raised when an error occurs while processing data retrieved from Wikipedia.

    Attributes:
        message (str): Description of the data processing error.
    """
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return self.message
