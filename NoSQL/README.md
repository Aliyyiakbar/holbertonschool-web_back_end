# NoSQL

This directory contains my solutions for the Holberton School project
**"NoSQL"**.

The goal of this project is to learn NoSQL databases, the differences between
SQL and NoSQL, ACID properties, document storage, NoSQL types and benefits,
and how to query, insert, update, and delete information from a NoSQL
database using MongoDB and PyMongo.

## Learning Objectives

- What NoSQL means
- What is the difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are the benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command Files

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using MongoDB (version 4.4)
- All files must end with a new line
- The first line of all files must be a comment: `// my comment`
- A `README.md` file at the root of this project folder is mandatory
- The length of your files will be tested using `wc`

### Python Scripts

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9) and `PyMongo` (version 4.8.0)
- All files must end with a new line
- The first line of all files must be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of this project folder is mandatory
- Code should use `pycodestyle` style (version 2.5.*)
- The length of your files will be tested using `wc`
- All modules must have documentation
- All functions must have documentation
- Code must not be executed when imported (by using `if __name__ == "__main__":`)

## Files

- `0-list_databases`
  Lists all databases in MongoDB.
- `1-create_database`
  Creates (switches to) a database in MongoDB.
- `2-insert_document`
  Inserts a document into a collection.
- `3-all_documents`
  Lists all documents in a collection.
- `4-match_documents`
  Lists all documents matching a given condition.
- `5-count`
  Counts the number of documents in a collection.
- `6-update`
  Updates a document in a collection.
- `7-delete`
  Deletes documents matching a given condition.
- `8-all.py`
  Lists all documents in a collection using PyMongo.
- `9-insert_school.py`
  Inserts a new document into a collection and returns its id.
- `10-update_topics.py`
  Changes all topics of a school document by name.
- `11-schools_by_topic.py`
  Returns the list of schools having a specific topic.
- `12-log_stats.py`
  Prints stats about Nginx logs stored in MongoDB.

## Usage

Example (MongoDB command file):

```bash
cat 0-list_databases | mongo
```

Example (Python script):

```bash
./8-all.py
```

## Author

Aliyyiakbar Shirinli
