#!/usr/bin/python3
"""Custom object serialization/deserialization with pickle"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, mode="wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError, EOFError):
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, mode="rb") as f:
                obj = pickle.load(f)
                return obj
        except (OSError, pickle.PickleError, EOFError):
            return None
