#!/usr/bin/python3
"""Defines Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of simple data structure."""
    return obj.__dict__

