#!/usr/bin/python3
# The Filedtorage class
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """class that serializes instances to a JSON file and deserializes\
            JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    className = {'BaseModel': BaseModel,
            'User' : User}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        j_objects = {}
        for key, val in FileStorage.__objects.items():
            j_objects[key] = val.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(j_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file exists
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                des = json.load(f)
                for k, v in des.items():
                    name = v['__class__']
                    obj_id = v['id']
                    self.__objects[obj_id] = FileStorage.className[name](**v)
                    self.new(self.__objects[obj_id])
        except FileNotFoundError:
            pass
