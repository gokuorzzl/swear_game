import functools


@functools.total_ordering
class Card:

    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        return self.num == other.num

    def __lt__(self, other):
        return self.num < other.num

    def __repr__(self):
        return '<Card({})>'.format(self.num)
    # 리프리젠테이션 해당객체>>문자열로 보여주게끔 동작함
