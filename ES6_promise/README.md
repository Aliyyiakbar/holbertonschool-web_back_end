# ES6 Promises

This directory contains my solutions for the Holberton School project
**"ES6 Promises"**.

The goal of this project is to learn Promises in JavaScript, including how to
use `then`, `resolve`, `catch`, and every method of the Promise object, as
well as `throw`/`try`, the `await` operator, and `async` functions.

## Learning Objectives

- Promises (how, why, and what)
- How to use the `then`, `resolve`, `catch` methods
- How to use every method of the Promise object
- `throw` / `try`
- The `await` operator
- How to use an `async` function

## Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Node.js 20.x.x and npm 9.x.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files must end with a new line
- A `README.md` file at the root of this project folder is mandatory
- Code must use the `.js` extension
- Code will be tested using Jest and the command `npm run test`
- Code will be verified against lint using ESLint
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
- `utils.js` — Helper functions `uploadPhoto` and `createUser` used by tasks

## Files

- `0-promise.js` — Returns a Promise from `getResponseFromAPI`.
- `1-promise.js` — Returns a Promise resolved/rejected based on success flag.
- `2-prime.js` — Appends handlers to a promise with `then` and `catch`.
- `3-allusers.js` — Handles multiple successful promises with `Promise.all`.
- `4-user-promise.js` — Creates a simple resolved promise.
- `5-photo-reject.js` — Rejects a promise with an error.
- `6-user-photo.js` — Handles multiple promises with `Promise.allSettled`.
- `7-load_balancer.js` — Returns the first resolved promise with `Promise.race`.
- `8-try.js` — Throws an error using async/try/catch.
- `9-try.js` — Throws error with try/catch and error handling.
- `100-await.js` — Await/Async to log values from a function (advanced).

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
