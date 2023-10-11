#!/usr/bin/python3
""" File Storage Class Module """
import json
from models.amenity import Amenity

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
         """Returns a dictionary of all objects"""
         return FileStorage.__objects

    def new(self, obj):
         """Adds a new object to the storage dictionary"""
         key = "{}.{}".format(obj.__class__.__name__, obj.id)
         FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the objects to a JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes objects from the JSON file"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    cls = models[class_name]
                    new_obj = cls(**value)
                    FileStorage.__objects[key] = new_obj

models = {
    'User': User,
    'State': State,
    'City': City,
    'Place': Place,
    'Amenity': Amenity,
    'Review': Review,
    'BaseModel': BaseModel,
}

storage = FileStorage()
storage.reload()
