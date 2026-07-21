#!/usr/bin/env python3
"""Return the list of schools having a specific topic."""
from typing import List, Dict, Any


def schools_by_topic(mongo_collection, topic: str) -> List[Dict[str, Any]]:
    """Return the list of schools having a specific topic.

    mongo_collection is the pymongo collection object.
    topic is the topic searched.
    """
    return [doc for doc in mongo_collection.find({"topics": topic})]
