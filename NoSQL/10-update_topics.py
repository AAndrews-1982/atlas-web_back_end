#!/usr/bin/env python3
"""
Module to update topics of a school document in a MongoDB collection.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school name.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

