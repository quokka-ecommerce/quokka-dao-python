# -*- coding: utf-8 -*-


class ProductReview(object):

    def __init__(self, product_id, user_id, content, star):
        self.product_id = product_id
        self.user_id = user_id
        self.content = content
        self.star = star

    @staticmethod
    def dummy():
        return ProductReview(1, 2, "hello", 5)

    def __dict__(self):
        return {
            "product_id": self.product_id,
            "user_id": self.user_id,
            "content": self.content,
            "star": self.star
        }


if __name__ == "__main__":
    p = ProductReview(1, 2, 3, 4)
    print p.__dict__()