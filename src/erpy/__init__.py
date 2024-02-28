from term import codec
from term.basetypes import Term
from typing import Generator

import struct
import sys


def _mailbox_gen() -> Generator[Term, None, None]:
    while True:
        len_bin = sys.stdin.buffer.read(4)
        if len(len_bin) != 4:
            return None
        (length,) = struct.unpack("!I", len_bin)
        (term, rest) = codec.decode(sys.stdin.buffer.read(length))
        yield term


def _port_gen() -> Generator[None, Term, None]:
    while True:
        term = codec.encode((yield))
        sys.stdout.buffer.write(struct.pack("!I", len(term)))
        sys.stdout.buffer.write(term)


def stdio_port_connection() -> (
    tuple[Generator[Term, None, None], Generator[None, Term, None]]
):
    port = _port_gen()
    next(port)
    return _mailbox_gen(), port
