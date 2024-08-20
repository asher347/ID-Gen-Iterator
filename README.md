# ID Validity Checker and Generator

## Overview

This project provides functionality for checking the validity of ID numbers and generating valid IDs using two approaches: an iterator and a generator. The ID validity is determined based on specific rules, and valid IDs can be generated sequentially from a starting point.

## Features

- **Check ID Validity**: Verify if an ID number is valid based on predefined rules.
- **ID Iterator**: Generate valid IDs using an iterator-based approach.
- **ID Generator**: Generate valid IDs using a generator-based approach.

## Functions

### `check_id_valid(id_number)`

Checks if the provided ID number is valid according to the following rules:
1. The ID must be at least 9 digits long.
2. Odd indices are multiplied by 1, and even indices are multiplied by 2.
3. If any resulting number is greater than 10, its digits are summed.
4. The ID is considered valid if the sum of all processed numbers is divisible by 10.

**Parameters:**
- `id_number` (int): The ID number to be checked.

**Returns:**
- `bool`: `True` if the ID is valid, `False` otherwise.

### `IDIterator`

A class that creates valid IDs using an iterator protocol.

**Constructor:**
- `__init__(self, id=100000000)`: Initializes the iterator with a starting ID (default is 100,000,000).

**Methods:**
- `__iter__(self)`: Returns the iterator object.
- `__next__(self)`: Returns the next valid ID. Raises `StopIteration` if the iterator exceeds 9 digits.

### `id_generator(id_number)`

A generator function that yields valid IDs starting from the given ID number.

**Parameters:**
- `id_number` (int): The starting ID number.

**Yields:**
- `int`: Valid IDs sequentially.

**Returns:**
- `str`: A message if the ID exceeds 9 digits.

## Usage

1. **Check ID Validity:**
   Call the `check_id_valid(id_number)` function with an ID number to check if it is valid.

2. **Generate Valid IDs Using Iterator:**
   Create an instance of `IDIterator` and call `next()` on it to get valid IDs.

3. **Generate Valid IDs Using Generator:**
   Use the `id_generator(id_number)` function to get a generator for valid IDs.
