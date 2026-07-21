# Pagination

This directory contains my solutions for the Holberton School project
**"Pagination"**.

The goal of this project is to learn how to paginate a dataset with simple
page and page_size parameters, with hypermedia metadata, and in a
deletion-resilient manner.

## Learning Objectives

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements

- A `README.md` file at the root of this project folder is mandatory
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
- All files must end with a new line
- The first line of all files must be exactly `#!/usr/bin/env python3`
- Code should use `pycodestyle` style (version 2.5.*)
- The length of your files will be tested using `wc`
- All modules must have documentation
- All functions must have documentation
- A documentation must be a real sentence explaining the purpose of the module, class, or method
- All functions and coroutines must be type-annotated

## Files

- `0-simple_helper_function.py`
  Returns a tuple of start/end indexes for a given page and page_size.
- `1-simple_pagination.py`
  Simple pagination of a dataset via a Server class get_page method.
- `2-hypermedia_pagination.py`
  Hypermedia pagination returning page data with metadata.
- `3-hypermedia_del_pagination.py`
  Deletion-resilient hypermedia pagination of a dataset.

## Usage

Example:

```bash
chmod +x 0-simple_helper_function.py
./0-main.py
```

## Author

Aliyyiakbar Shirinli
