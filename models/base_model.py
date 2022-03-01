#!/usr/bin/python3
"""Create class BaseModel that defines all common
   attributes/methods for other class
"""
from uuid import uuid4
from datetime import datetime



class BaseModel:
    """Create a BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Public instance attribute"""
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    iso_time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, iso_time)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Print id and dict"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Updates a Base Model instance
        Updates the public instance attribute `updated_at`
        with the current datetime and dumps the class data
        into a file
        """
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing
        all keys/values of __dict__
        """
        dict_n = self.__dict__.copy()
        dict_n.update({"__class__": self.__class__.__name__})
        dict_n.update({"created_at": self.created_at.isoformat()})
        dict_n.update({"updated_at": self.updated_at.isoformat()})
        return (dict_n)
