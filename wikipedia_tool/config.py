"""
Configuration module for wikipedia_tool.

This module provides a robust configuration system for setting and managing
parameters used throughout the wikipedia_tool library. It supports default
values, environment variable overrides, and dynamic updates.
"""

import os
import json
from typing import Dict, Any


class Config:
    """
    A configuration class for wikipedia_tool settings.

    Attributes:
        API_URL (str): The default Wikipedia API endpoint.
        LANGUAGE (str): The default language for API queries.
        USER_AGENT (str): The user agent string used in HTTP requests.
        TIMEOUT (int): The timeout in seconds for API requests.
        PROXIES (Dict[str, str]): Proxy configuration for HTTP requests.
        EXTRA_PARAMS (Dict[str, Any]): Additional parameters for API calls.
    """

    def __init__(self) -> None:
        self.API_URL: str = os.environ.get("WIKIPEDIA_API_URL", "https://en.wikipedia.org/w/api.php")
        self.LANGUAGE: str = os.environ.get("WIKIPEDIA_LANGUAGE", "en")
        self.USER_AGENT: str = os.environ.get("WIKIPEDIA_USER_AGENT", "wikipedia_tool/1.0 (https://github.com/yourusername/wikipedia-tool)")
        self.TIMEOUT: int = int(os.environ.get("WIKIPEDIA_TIMEOUT", "10"))
        self.PROXIES: Dict[str, str] = {}
        proxies_env: str = os.environ.get("WIKIPEDIA_PROXIES", "")
        if proxies_env:
            try:
                self.PROXIES = json.loads(proxies_env)
            except Exception:
                self.PROXIES = {}
        self.EXTRA_PARAMS: Dict[str, Any] = {}

    def update(self, config_updates: Dict[str, Any]) -> None:
        """
        Update configuration parameters with the provided dictionary.

        Args:
            config_updates (Dict[str, Any]): A dictionary containing configuration updates.
        """
        for key, value in config_updates.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                self.EXTRA_PARAMS[key] = value

    def as_dict(self) -> Dict[str, Any]:
        """
        Return the current configuration as a dictionary.

        Returns:
            Dict[str, Any]: A dictionary representation of the configuration.
        """
        return {
            "API_URL": self.API_URL,
            "LANGUAGE": self.LANGUAGE,
            "USER_AGENT": self.USER_AGENT,
            "TIMEOUT": self.TIMEOUT,
            "PROXIES": self.PROXIES,
            "EXTRA_PARAMS": self.EXTRA_PARAMS,
        }


config = Config()
