#!/usr/bin/python3
""" Initializing models as a package """
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
