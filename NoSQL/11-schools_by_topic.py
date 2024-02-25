#!/usr/bin/env python3
"""
Module to find schools by topic in a MongoDB collection.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)

