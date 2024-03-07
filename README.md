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

### Sending Messages From Python

```python
from erpy import stdio_port_connection

inbox, port = stdio_port_connection()
for i in range(100):
    port.send(i)

```

### Receiving Messages In Python

```python
from erpy import stdio_port_connection
from term import Atom

inbox, port = stdio_port_connection()

for msg in inbox:
    if msg == Atom("close"):
        break
    
    with open("output.txt", "a") as f:
        print(f"got {msg}", file=f)
```
