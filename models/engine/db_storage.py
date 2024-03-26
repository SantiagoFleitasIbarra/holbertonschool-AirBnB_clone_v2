#!/usr/bin/python3
""""""
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
import os


class DBStorage():
    """"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        database = os.getenv('HBNB_MYSQL_DB')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db_uri = f"mysql+mysqldb://{user}:{password}@{host}/{database}"
        self.__engine = create_engine(db_uri, pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            pass