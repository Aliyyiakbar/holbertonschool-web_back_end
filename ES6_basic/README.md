# ES6 Basics

This directory contains my solutions for the Holberton School project
**"ES6 Basics"**.

The goal of this project is to learn ECMAScript 6 (ES2015), including the new
features it introduced such as block-scoped variables (`const`/`let`), arrow
functions, default and rest/spread parameters, template literals, object
property shorthand and method properties, iterables and iterators, and the
`for...of` loop.

## Learning Objectives

- What ES6 is
- New features introduced in ES6
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and function parameters default to them
- Rest and spread function parameters
- String templating in ES6
- Object creation and their properties in ES6
- Iterators and `for...of` loops

## Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Node.js 20.x.x and npm 9.x.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files must end with a new line
- A `README.md` file at the root of this project folder is mandatory
- Code must use the `.js` extension
- Code will be tested using the Jest Testing Framework
- Code will be analyzed using the linter ESLint with the provided rules
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

- `0-constants.js` — Uses `const` and `let` instead of `var`.
- `1-block-scoped.js` — Block-scoped variables with `let` and `const`.
- `2-arrow.js` — Arrow functions.
- `3-default-parameter.js` — Default function parameters.
- `4-rest-parameter.js` — Rest parameter syntax.
- `5-spread.js` — Spread syntax.
- `6-string-interpolation.js` — Template literals.
- `7-getBudgetObject.js` — Object property value shorthand.
- `8-getBudgetCurrentYear.js` — Computed property names.
- `9-sectors.js` — ES6 method properties.
- `10-loops.js` — `for...of` loop.
- `11-createEmployeesObject.js` — Iterator creation.
- `12-createReportObject.js` — Report object with iterator.
- `100-iterate-through-object.js` — Iterating through report objects (advanced).
- `101-iterate-through-object.js` — Iterate through object (advanced).

## Usage

Example:

```bash
npm run dev 0-main.js
```

Run tests:

```bash
npm test
```

Run lint:

```bash
npm run lint
```

## Author

Aliyyiakbar Shirinli
