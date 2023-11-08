#!/usr/bin/python3
""" class-to-JSON module."""


def class_to_json(obj):
    """Return the dictionary represntation of json JSON serialization of an object:"""
    return obj.__dict__
