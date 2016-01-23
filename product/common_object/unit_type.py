# -*- coding: utf-8 -*-

from flufl.enum import Enum


class UnitType(Enum):
    BAG = u"袋"
    PACKAGE = u"包"
    BOX = u"盒"
    GRAM = u"克"
    KILOGRAM = u"千克"
    TYPE = u"TYPE"

    @staticmethod
    def from_string(string):
        pass


if __name__ == "__main__":
    print UnitType(u"千克")
