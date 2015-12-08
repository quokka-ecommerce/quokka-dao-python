# -*- coding: utf-8 -*-

from product_unit import ProductUnit
from product_review import ProductReview

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

    @staticmethod
    def not_none(field, field_name):
        if field is None:
            raise ValueError(field_name + " should not be None")

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

        if not isinstance(self.product_unit, ProductUnit):
            raise TypeError("product unit should be ProductUnit Type")

        if not isinstance(self.attributes, list):
            raise TypeError("attributes should be a list")

        for item in self.attributes:
            if not isinstance(item, dict):
                raise TypeError("attribute should be a dict")

        if not isinstance(self.reviews, list):
            raise TypeError("reviews should be list")

        for item in self.reviews:
            if not isinstance(item, ProductReview):
                raise TypeError("review should be a ProductReview")


if __name__ == "__main__":
    pass