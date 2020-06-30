#!/usr/bin/python3
"""New engine DBStorage
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """New engine DBStorage
    """
    _engine = None
    __session = None
    classes = ["State", "City", "User", "Place", "Review", "Amenity"]

    def __init__(self):
        """ Init method for DBStorage class
        """
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Select all classes
        """
        dictt = {}
        if cls is not None:
            sel = self.__session.query(cls).all()
            for r in sel:
                key = cls.__name__ + '.' + r.id
                dictt[key] = r
            return dictt
        else:
            for classe in self.classes:
                try:
                    for obj in self.__session.query(eval(classe)).all():
                        ob = classe + '.' + obj.id
                        dictt[ob] = obj
                except:
                    pass
            return dictt

    def new(self, obj):
        """ Add object to the database
        """
        self.__session.add(obj)

    def save(self):
        """ Commits changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete object from the database
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create the tables in databas
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(expire_on_commit=False)
        self.session = session_factory.configure(bind=self.__engine)
        Session = scoped_session(session_factory)
        self.__session = Session()

        def close(self):
        """close"""
        self.__session.remove()
