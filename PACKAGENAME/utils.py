import os
from typing import Callable, List


def fileToList(filename: str, strconv: Callable[[str], str] = lambda x: x) -> List[str]:
    """
    loads an input file with a\\n b\\n.. into a list [a,b,..]
    """
    with open(filename) as f:
        return [strconv(val[:-1]) for val in f.readlines()]


def listToFile(
    filename: str, lst: List[str], strconv: Callable[[str], str] = lambda x: x
):
    """
    writes a list to a file with a\\n b\\n..
    """
    with open(filename, "w") as f:
        f.write("\n".join([strconv(val) for val in lst]))


FILEDIR = os.path.dirname(os.path.realpath(__file__))
