#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Create class BaseModel that defines all common
   attributes/methods for other class
"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """Base Model Class
    This is the Base Model that take care of the
    initialization, serialization and deserialization
    of the future instances.
    """
    def __init__(self, *args, **kwargs):
        """Base Model __init__ Method
        Here, the default values of a Base Model
        instance are initialized.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                """loop through the key and its corresponding value"""
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                    """we convert to dictionary key with the
                    given value of the time string
                    """
                else:
                    if key != "__class__":
                        self.__dict__[key] = value
                        """if key is not found in __class__ , we must add
                        the value to
                        this dictionary with the object's class name
                        """
        else:
            models.storage.new(self)

    def __str__(self):
        """Representation of the class for the user
        Example:
            $ bm = BaseModel()
            $ print(bm)
            This method prints the content of the Base Model
            class with this format
            $ [<class name>] (<self.id>) <self.__dict__>
        """
        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """Updates a Base Model instance
        Updates the public instance attribute `updated_at`
        with the current datetime and dumps the class data
        into a file
        """
        self.updated_at = datetime.now()
        models.storage.save(self)

    def to_dict(self):
        """Converts the information of the class to human-readable format
        Returns a new dictionary containing all keys/values
        of __dict__ of the instance.
        """
        dict_n = self.__dict__.copy()
        dict_n['__class__'] = self.__class__.__name__
        dict_n['created_at'] = self.created_at.isoformat()
        dict_n['updated_at'] = self.updated_at.isoformat()

        return dict_n
