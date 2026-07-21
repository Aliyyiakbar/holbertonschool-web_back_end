# ES6 Classes

This directory contains my solutions for the Holberton School project
**"ES6 Classes"**.

The goal of this project is to learn ES6 classes, including how to define a
class, add methods and static methods, extend a class from another, and use
metaprogramming with symbols.

## Learning Objectives

- How to define a Class
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols

## Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Node.js 20.x.x and npm 9.x.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files must end with a new line
- A `README.md` file at the root of this project folder is mandatory
- Code must use the `.js` extension
- Code will be tested using Jest and the command `npm run test`
- Code will be verified against lint using ESLint
- Code needs to pass all the tests and lint (`npm run full-test`)

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

- `0-classroom.js` — ClassRoom class with a `_maxStudentsSize` attribute.
- `1-makeClassrooms.js` — Initializes an array of ClassRoom instances.
- `2-hbtnCourse.js` — HolbertonCourse class with getters and setters.
- `3-currency.js` — Currency class with computed method names.
- `4-pricing.js` — Pricing class composing Currency.
- `5-building.js` — Building class with an abstract evacuationWarning.
- `6-skyHigh.js` — SkyHighBuilding extending Building.
- `7-airport.js` — Airport class with toString symbol.
- `8-hbtnClass.js` — HolbertonClass using primitive casting symbols.
- `9-hoisting.js` — Fix hoisting issues with class declarations.
- `10-car.js` — Car class with clone symbol.
- `100-evcar.js` — EVCar extending Car with cloning (advanced).

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
