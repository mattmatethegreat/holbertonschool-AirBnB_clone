#!/usr/bin/python3

from models.base_model import BaseModel
""" State Class """
class State(BaseModel):
    """ State Class """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
