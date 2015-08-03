import functools


@functools.total_ordering
class Card:

    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        return self.num == other.num

    def __lt__(self, other):
        return self.num < other.num
