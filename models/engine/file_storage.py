#!/usr/bin/python3
"""Serializes instances to a JSON file and.
   deserializes JSON file to instances
"""
import json


class FileStorage():
    """File Storage Class
    This is the File Storage module.
    Attributes:
        __file_path (str): This is the path of the JSON file in which
            the contents of the `__objects` variable will be stored.
        __objects (dict): This store all the instances data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Gets the __objects info
        Returns the content of the `__objects` class attribute.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Saves a new object in the `__objects` class attribute
        Args:
            obj (inst): The object to adds in the `__objects` class attribute
        Sets in the `__objects` class attribute the instance data
        with a key as <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the content of `__objects` class attribute
        The content of `__objects` class attribute will be serialized
        to the path of `__file_path` class attribute in JSON format
        with the `created_at` and `updated_at` formatted.
        """
        json_dict = {}
        with open(self.__file_path, mode='w', encoding='utf-8') as my_file:
            for key, value in FileStorage.__objects.items():
                json_dict.update({key: value.to_dict()})
            my_file.write(json.dumps(json_dict))

    def reload(self):
        """Deserializes the JSON file in `__file_path` class attribute
        If the file on `__file_path` class attribute exists, each object
        on the file will be deserialized and appended to the `__objects`
        class attribute like an instance with the object data.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as my_file:
                json_dict = json.loads(my_file.read())
                for key, value in json_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
