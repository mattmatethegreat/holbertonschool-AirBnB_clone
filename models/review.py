#!/usr/bin/python3
from models.base_model import BaseModel
""" Review Class """
class Review(BaseModel):
    """ Review Class """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
