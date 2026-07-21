#!/usr/bin/env python3
"""Return all students sorted by average score using MongoDB aggregation."""
from typing import List, Dict, Any


def top_students(mongo_collection) -> List[Dict[str, Any]]:
    """Return all students sorted by average score.

    mongo_collection is the pymongo collection object.
    The average score is added to each item with the key averageScore.
    """
    pipeline = [
        {"$addFields": {
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
