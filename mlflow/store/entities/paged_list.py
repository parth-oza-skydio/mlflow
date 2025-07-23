import typing

from typing import TypeVar

T = TypeVar("T")


class PagedList(typing.List[T]):
    """
    Wrapper class around the base Python `List` type. Contains an additional `token`  string
    attribute that can be passed to the pagination API that returned this list to fetch additional
    elements, if any are available
    """

    def __init__(self, items: typing.List[T], token):
        super().__init__(items)
        self.token = token

    def to_list(self):
        return list(self)
