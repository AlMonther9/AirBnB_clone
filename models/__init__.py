#!/usr/bin/python3
"""This module creates an instance of the FileStorage class."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()  # Load data from the JSON file into the storage
