# -*- coding: utf-8 -*-

from unit_type import UnitType


class ProductUnit(object):

    def __init__(self, unit_type, unit_number):
        if not isinstance(unit_type, UnitType.TYPE.__class__):
            raise TypeError, "unit_type should be UnitType enum"
        if not isinstance(unit_number, int):
            raise TypeError, "unit_number shoud be int"
        self.unit_type = unit_type
        self.unit_number = unit_number

    def __dict__(self):
        current_dict = {
            "unit_type": self.unit_type.value,
            "unit_number": self.unit_number
        }
        return current_dict

    def __str__(self):
        return str(self.__dict__())

    def __repr__(self):
        return "unit_type: " + self.unit_type.value + ", unit_number: " + str(self.unit_number)

    @staticmethod
    def dummy():
        dummy_type = UnitType.BAG
        dummy_number = 1
        return ProductUnit(dummy_type, dummy_number)


if __name__ == "__main__":
    t = UnitType.BAG
    p = ProductUnit(t, 1)
    print repr(p)


