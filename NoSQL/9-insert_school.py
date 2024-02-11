#!/usr/bin/env python3
"""
Module to insert a new document in a MongoDB collection based on kwargs.
"""

from bson.objectid import ObjectId

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

