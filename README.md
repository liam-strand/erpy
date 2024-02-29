# ERPY

This library wraps around the Python version of the Term library to provide
a simple mechanism for communicating between an Erlang process and a Python
process.

## Installation

As always, use `pip`, preferably within a virtual environment.

```
pip install erpy
```

## Usage

### Encoding and Decoding Erlang Terms

Use the `term` library. Their documentation is [here](https://pyrlang.github.io/Term/), 
and the python version of their library is bundled with this library. If you 
want to get the Rust one working with PyPi, I'm sure that they would apprecate 
it `:)`.

## Basic Communication over STDIO

Pattern matching is
