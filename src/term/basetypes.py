from typing import Union, List


class BaseTerm:
    """ Base class for all Erlang terms. """
    pass


class BasePid(BaseTerm):
    """ Serves as a base for local pid and remote pid. """
    pass


class BaseRef(BaseTerm):
    """ Serves as a base for local ref and remote ref. """
    pass


# Type AnyTerm includes Erlang type wrappers + compatible Python types
Term = Union[str, List["Term"], tuple, dict, int, float, bytes, BaseTerm, None]
