# UTF-8 Validation

This project involves implementing a Python method that validates whether a given dataset represents a valid UTF-8 encoding. The UTF-8 encoding scheme allows characters to be encoded into one to four bytes, and this validation checks whether the dataset follows these encoding rules.

## Table of Contents

- [Requirements](#requirements)
- [Concepts Utilized](#concepts-utilized)
- [Function Prototype](#function-prototype)
- [Usage](#usage)
- [Example](#example)
- [Installation](#installation)
- [Testing](#testing)
- [License](#license)

## Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- All files should end with a new line.
- The first line of all files should be `#!/usr/bin/python3`.
- A `README.md` file at the root of the folder is mandatory.
- Code should follow PEP 8 style guidelines (version 1.7.x).
- All files must be executable.

## Concepts Utilized

To effectively implement the UTF-8 validation, the following concepts and techniques are essential:

- **Bitwise Operations in Python**: Understanding how to manipulate bits using operations such as AND (`&`), OR (`|`), shifts (`<<`, `>>`), etc.
- **UTF-8 Encoding Scheme**: Familiarity with how UTF-8 encodes characters into one to four bytes.
- **Data Representation**: Handling data at the byte level and manipulating the least significant bits.
- **List Manipulation in Python**: Iterating through and processing lists of integers.
- **Boolean Logic**: Applying logical operations to determine the validity of the encoding.

## Function Prototype

```python
def validUTF8(data: list[int]) -> bool:
    """
    Determines if a given dataset represents a valid UTF-8 encoding.

    :param data: List of integers, each representing a byte (8 bits).
    :return: True if the data is a valid UTF-8 encoding, False otherwise.
    """
```

## Usage

To use the `validUTF8` method, you can import it from the `0-validate_utf8.py` file and pass a list of integers representing the dataset to be validated.

Example usage:

```python
validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Output: True
```

## Example

Here are some test cases demonstrating the expected output:

```python
data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/alx-interview.git
cd alx-interview/0x04-utf8_validation
```

Ensure you have Python 3 installed and run the script using:

```bash
./0-main.py
```

## Testing

Testing can be performed by executing the main file or writing additional test cases. Ensure that all edge cases are handled, especially those involving multi-byte characters and invalid byte sequences.

## License

This project is licensed under the MIT License.