#!/usr/bin/env python3
"""Change all topics of a school document based on the name."""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """Change all topics of a school document based on the name.

    mongo_collection is the pymongo collection object.
    name is the school name to update.
    topics is the list of topics approached in the school.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
