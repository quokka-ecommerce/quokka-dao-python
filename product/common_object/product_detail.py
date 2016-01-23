# -*- coding: utf-8 -*-

from product_unit import ProductUnit
from product_review import ProductReview


def to_unicode(string):
    try:
        return string.decode("UTF-8")
    except:
        return string


class ProductDetail(object):

    def __init__(self, id, product_name, upc, category_l1, category_l2, category_l3, product_unit, brand, original_country,
                 attributes, current_price, current_stock, image_link, product_description, vendor_id, sale_history_id,
                 history_price, reviews):
        self._id = id
        self.product_name = product_name
        self.upc = upc
        self.category_l1 = category_l1
        self.category_l2 = category_l2
        self.category_l3 = category_l3
        self.product_unit = product_unit
        self.brand = brand
        self.original_country = original_country
        self.attributes = attributes
        self.current_price = current_price
        self.current_stock = current_stock
        self.image_link = image_link
        self.product_description = product_description
        self.vendor_id = vendor_id
        self.sale_history_id = sale_history_id
        self.history_price = history_price
        self.reviews = reviews
        # self.validate()

    @staticmethod
    def not_none(field, field_name):
        if field is None:
            raise ValueError(field_name + " should not be None")

    @staticmethod
    def instance_check(field, field_name, field_type):
        if field is None:
            return
        if not isinstance(field, field_type):
            string = "{0} should be type of {1}"
            raise TypeError(string.format(field_name, field_type))

    @staticmethod
    def dummy():
        dummy_attribute = {
            "core": 4,
            "cpu": "i5"
        }
        dummy_unit = ProductUnit.dummy()
        dummy_review = ProductReview.dummy()
        return ProductDetail(
            1L,
            "dummy",
            123456L,
            "l1", "l2", "l3",
            dummy_unit, "apple", "china", dummy_attribute,
            13.2, 12, "http://image.com", "good product",
            123L, 234L, float(1.9), [dummy_review, dummy_review]
        )

    def validate(self):
        ProductDetail.not_none(self._id, "id")
        ProductDetail.not_none(self.product_name, "product name")
        ProductDetail.not_none(self.category_l1, "category l1")
        ProductDetail.not_none(self.category_l2, "category l2")
        ProductDetail.not_none(self.category_l3, "category l3")
        ProductDetail.not_none(self.original_country, "original country")
        ProductDetail.not_none(self.product_unit, "prodcut unit")
        ProductDetail.not_none(self.brand, "brand")
        ProductDetail.not_none(self.current_stock, "current stock")
        ProductDetail.not_none(self.current_price, "current_price")
        ProductDetail.not_none(self.image_link, "image_link")

        ProductDetail.instance_check(self.upc, "upc", long)
        ProductDetail.instance_check(self._id, "id", long)
        ProductDetail.instance_check(self.vendor_id, "vendor", long)
        ProductDetail.instance_check(self.sale_history_id, "sale history", long)
        ProductDetail.instance_check(self.history_price, "history price", float)
        ProductDetail.instance_check(self.product_unit, "product_unit", ProductUnit)
        ProductDetail.instance_check(self.category_l1, "l1 category", unicode)
        ProductDetail.instance_check(self.category_l2, "l2 category", unicode)
        ProductDetail.instance_check(self.category_l3, "l3 category", unicode)


        ProductDetail.instance_check(self.attributes, "product attributes", dict)
        ProductDetail.instance_check(self.reviews, "reviews", list)
        for item in self.reviews:
            ProductDetail.instance_check(item, "review", ProductReview)

    def __dict__(self):
        current_dict = {
            "id": self._id,
            "product_name": self.product_name,
            "upc": self.upc,
            "category_l1": self.category_l1,
            "category_l2": self.category_l2,
            "category_l3": self.category_l3,
            "brand": self.brand,
            "original_country": self.original_country,
            "current_price": self.current_price,
            "current_stock": self.current_stock,
            "image_link": self.image_link,
            "product_description": self.product_description,
            "vendor_id": self.vendor_id,
            "sale_history_id": self.sale_history_id,
            "history_price": self.history_price,
        }
        current_dict.update(self.product_unit.__dict__())
        current_dict.update({"attribute": self.attributes})
        current_dict.update({"review": map(lambda x: x.__dict__(), self.reviews)})
        return current_dict

    @staticmethod
    def build(string_dict):
        return ProductDetail(
            id=long(string_dict['id']),
            product_name=to_unicode(string_dict['product_name']),
            upc=long(string_dict['upc']),
            category_l1=to_unicode(string_dict['category_l1']),
            category_l2=to_unicode(string_dict['category_l2']),
            category_l3=to_unicode(string_dict['category_l3']),
            product_unit=ProductUnit.build(string_dict),
            brand=to_unicode(string_dict['brand']),
            original_country=to_unicode(string_dict['original_country']),
            attributes=ProductDetail.build_arrtibute(string_dict),
            current_price=to_unicode(string_dict['current_price']),
            current_stock=to_unicode(string_dict['current_stock']),
            image_link=to_unicode(string_dict['image_link']),
            product_description=to_unicode(string_dict['product_description']),
            vendor_id=long(string_dict['vendor_id']),
            sale_history_id=long(string_dict['sale_history_id']),
            history_price=float(string_dict['history_price']),
            reviews=[],
        )

    @staticmethod
    def build_arrtibute(string_dict):
        attribute_dict = {}
        for key in string_dict.keys():
            if str(key).startswith("attr_"):
                attribute_dict[to_unicode(key)] = to_unicode(string_dict[key])
        return attribute_dict

if __name__ == "__main__":
    d = ProductDetail.dummy()
    print d.__dict__()
