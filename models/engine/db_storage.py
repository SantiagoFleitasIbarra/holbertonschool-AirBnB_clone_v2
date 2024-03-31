#!/usr/bin/python3
""""""
from models.base_model import Base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """"""
    __engine = None
    __session = None
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        database = os.getenv('HBNB_MYSQL_DB')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db_uri = f"mysql+mysqldb://{user}:{password}@{host}/{database}"
        self.__engine = create_engine(db_uri, pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            metadata = MetaData()
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        objects = {}

        if cls:
            if cls.__name__ in self.classes:
                objects = self.__session.query(cls).all()
        else:
            for cls_name in self.classes:
                cls = globals().get(cls_name)
                if cls:
                    objects.update({obj.id: obj for obj in self.__session.query(cls).all()})
        return objects

    def new(self, obj):
        if obj:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()