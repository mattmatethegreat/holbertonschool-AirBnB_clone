#!/usr/bin/python3
from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Amenity Class """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""

    def to_dict(self):
        amenity_dict = super().to_dict()
        amenity_dict.update({
            "name": self.name,
        })
        return amenity_dict
