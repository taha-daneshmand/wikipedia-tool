"""
Utility functions for wikipedia_tool.

This module provides various helper functions such as retry decorators, string slugification,
title normalization, dictionary merging, safe JSON parsing, and query parameter conversion.
These utilities are designed to support robust operations throughout the wikipedia_tool library.
"""

import functools
import time
import re
import json
from typing import Any, Callable, Dict, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def retry(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0, exceptions: tuple = (Exception,)) -> Callable[[F], F]:
    """
    Decorator that retries a function call on specified exceptions with exponential backoff.

    Args:
        max_attempts (int): Maximum number of attempts before giving up.
        delay (float): Initial delay between attempts in seconds.
        backoff (float): Multiplicative backoff factor for delay.
        exceptions (tuple): Tuple of exception classes to catch and retry on.

    Returns:
        Callable: The decorated function with retry logic.
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper  # type: ignore
    return decorator


def slugify(text: str) -> str:
    """
    Convert the given text to a slug suitable for URLs.

    Args:
        text (str): The input text.

    Returns:
        str: A slugified version of the text.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', ' ', text)
    text = text.strip()
    slug = re.sub(r'\s', '-', text)
    return slug


def normalize_title(title: str) -> str:
    """
    Normalize a Wikipedia page title by capitalizing the first letter and replacing underscores with spaces.

    Args:
        title (str): The original page title.

    Returns:
        str: The normalized title.
    """
    title = title.replace("_", " ").strip()
    if title:
        title = title[0].upper() + title[1:]
    return title


def merge_dicts(*dicts: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Merge multiple dictionaries into one. In case of key conflicts, later dictionaries override earlier ones.

    Args:
        *dicts (Dict[Any, Any]): Arbitrary number of dictionaries.

    Returns:
        Dict[Any, Any]: The merged dictionary.
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result


def safe_json_loads(s: str) -> Any:
    """
    Safely parse a JSON string and return the corresponding Python object.
    If parsing fails, returns None.

    Args:
        s (str): The JSON string.

    Returns:
        Any: The parsed JSON object, or None if parsing fails.
    """
    try:
        return json.loads(s)
    except Exception:
        return None


def dict_to_query_params(params: Dict[str, Any]) -> str:
    """
    Convert a dictionary of parameters into a URL query string.

    Args:
        params (Dict[str, Any]): Dictionary of query parameters.

    Returns:
        str: A URL-encoded query string.
    """
    parts = []
    for key, value in params.items():
        parts.append(f"{key}={value}")
    return "&".join(parts)


def parse_query_string(query: str) -> Dict[str, str]:
    """
    Parse a URL query string into a dictionary of parameters.

    Args:
        query (str): The query string.

    Returns:
        Dict[str, str]: A dictionary of query parameters.
    """
    pairs = query.split("&")
    result = {}
    for pair in pairs:
        if "=" in pair:
            key, value = pair.split("=", 1)
            result[key] = value
    return result
