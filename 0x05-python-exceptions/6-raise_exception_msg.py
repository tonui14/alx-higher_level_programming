#!/usr/bin/env python3

def raise_exception_msg(message=""):
    """
    Raise a NameError exception with a message.

    Args:
        message (str): The message to include in the exception.

    Raises:
        NameError: Always raises a NameError with the provided message.
    """
    raise NameError(message)
