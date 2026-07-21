# ES6 Data Manipulation

This directory contains my solutions for the Holberton School project
**"ES6 Data Manipulation"**.

The goal of this project is to learn how to manipulate data using ES6 array
methods (`map`, `filter`, `reduce`), typed arrays, and the `Set`, `Map`, and
`WeakMap` data structures.

## Learning Objectives

- How to use `map`, `filter`, and `reduce` on arrays
- Typed arrays
- The `Set`, `Map`, and `WeakMap` data structures

## Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Node.js 20.x.x and npm 9.x.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files must end with a new line
- A `README.md` file at the root of this project folder is mandatory
- Code must use the `.js` extension
- Code will be tested using Jest and the command `npm run test`
- Code will be verified against lint using ESLint
- Code needs to pass all the tests and lint (`npm run full-test`)
- All functions must be exported

## Setup

Install Node.js 20.x.x and the project dependencies (Jest, Babel, ESLint):

```bash
npm install
```

The project includes the following configuration files:

- `package.json` — scripts and dev dependencies
- `babel.config.js` — Babel preset configuration
- `.eslintrc.js` — ESLint rules (airbnb-base + jest)

## Files

- `0-get_list_students.js` — Returns an array of student objects.
- `1-get_list_student_ids.js` — Maps student objects to their ids.
- `2-get_students_by_loc.js` — Filters students by location.
- `3-get_ids_sum.js` — Reduces student ids to their sum.
- `4-get_ids_avg.js` — Computes the average of student ids.
- `5-typed_arrays.js` — Creates and manipulates a typed array.
- `6-set.js` — Creates a Set from an array.
- `7-has_array_values.js` — Checks if all values are present in a Set.
- `8-clean_set.js` — Cleans a Set by filtering values starting with a string.
- `9-groceries_list.js` — Creates a Map representing a groceries list.
- `10-update_uniq_items.js` — Updates a Map with unique items.
- `100-weak.js` — WeakMap data structure for tracking API calls (advanced).

## Usage

Example:

```bash
npm run dev 0-main.js
```

Run tests:

```bash
npm test
```

Run full test (lint + tests):

```bash
npm run full-test
```

## Author

Aliyyiakbar Shirinli
