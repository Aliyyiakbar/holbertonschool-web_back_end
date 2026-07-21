#!/usr/bin/env python3
"""Insert a new document in a collection based on kwargs."""
from typing import Any


def insert_school(mongo_collection, **kwargs) -> Any:
    """Insert a new document in a collection based on kwargs.

    mongo_collection is the pymongo collection object.
    Returns the new _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
