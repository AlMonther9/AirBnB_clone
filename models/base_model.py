#!/usr/bin/python3
"""This module defines a base class for all models in our HBNB clone project"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all models in the HBNB project."""

    def __init__(self, *args, **kwargs):
        """Creates a new instance of the model."""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Provides a string representation of the instance."""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at'
          attribute with the current time when the instance is changed

        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Converts instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
