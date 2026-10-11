#!/usr/bin/python3
"""Module for JSON serialization/deserialization"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary, save to JSON file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON data from file and return as dictionary"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.loaf(f)
