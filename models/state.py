#!/usr/bin/python3
"""This is the state class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel,Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="save-update, delete")

    @property
    def cities(self):
        """
        """
        citty = models.storage.all(City)
        dictt = {}
        for key, value in citty.items():
            if value.id == self.id:
                dictt[key] = value
        return dictt
