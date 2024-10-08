# DSA Project Documentation

Welcome to andy4747/dsa Project's documentation

```{toctree}
:maxdepth: 2
:caption: Contents

algorithms
data_structures
leetcode
neetcode
```

## Project Structure

```
/
│
├── src/
│   ├── algorithms/
│   ├── data_structures/
│   ├── leetcode/
│   └── neetcode/
│
├── tests/
│   └── test_all.py
│
└── docs/
    ├── conf.py
    └── index.md
```

## Clone Repository

To clone this project in your local environment:
```bash
git clone https://github.com/andy4747/dsa.git
```

## Installation

To install the project for development:

```bash
make dev-install
```

## Running Tests

To run all tests:

```bash
make test
```

To run a specific test:

```bash
make test-function FUNC=test_rotate_array
```
