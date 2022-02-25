class Product:
    def __init__(self, value):
        self.value = value


a = Product(12)
b = Product(7)
c = Product(10)
my_list_product = [a, b, c]

res_list_product = [product for product in my_list_product if product.value > 10]
res_list_product2 = list(filter(lambda obj: obj.value > 10, my_list_product))
