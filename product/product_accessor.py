from pymongo import MongoClient
from common_object.product_detail import ProductDetail


class ProductClient(object):
    def __init__(self):
        try:
            self.client = MongoClient("52.34.52.245", 27017)
        except Exception as e:
            print "error in init mongo client", e
        try:
            self.db_instance = self.client['test']
        except Exception as e:
            print "error in get db instance", e
        try:
            self.collection = self.db_instance['product']
        except Exception as e:
            print "error in get db instance", e

    def is_product_existed(self, product):
        if type(product) != ProductDetail:
            raise TypeError("except ProductDetail")
        post = self.collection.find({"product_name": product.product_name})
        return (post.count() != 0)

    def insert_product_detail_in_batch(self, products):
        for product in products:
            self.insert_product_detail(product)

    def insert_product_detail(self, product):
        if type(product) == ProductDetail:
            if self.is_product_existed(product):
                print "product exists"
                return
            post = product.__dict__()
            post_id = self.collection.insert_one(post)
            print post_id
        elif type(product) == list:
            for item in product:
                if self.is_product_existed(item):
                    print "product exists"
                    return
                post = item.__dict__()
                post_id = self.collection.insert_one(post)
                print post_id

    def fetch_all_product(self):
        data_cursor = self.collection.find()
        data = []
        for item in data_cursor:
            data.append(item)
        return data

    def __del__(self):
        self.client.close()
        print "disconnect client"


if __name__ == "__main__":
    client = ProductClient()
    print client.fetch_all_product()
    product = ProductDetail.dummy()
    client.insert_product_detail(product)


