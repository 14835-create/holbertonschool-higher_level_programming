#!/usr/bin/python3
"""Defines the city."""

from sqlalchemy import Column, Interger, String, ForeignKey
from sqlalchemy.orm import declarative_base
from model_state import Base


class city(Base):
    """Represents a city linked state."""

    __tablename__ = "cities"

    id = Column(Interger, primary_key=True, nullable=False)
    name = Column(string(128), nullable=False)
    state_id = Column(Interger, ForeignKey("states.id"), nullable=False)
