#!/usr/bin/env python3
"""List all documents in a collection using PyMongo."""
from typing import List, Dict, Any


def list_all(mongo_collection) -> List[Dict[str, Any]]:
    """List all documents in a collection.

    Return an empty list if no document in the collection.
    mongo_collection is the pymongo collection object.
    """
    return [doc for doc in mongo_collection.find()]
