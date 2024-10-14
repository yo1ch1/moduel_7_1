


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            products = file.read()
        file.close()
        return products

    def add(self, *products):
        with open(self.__file_name, 'r') as file:
            existing_products = file.read().split('\n')
            existing_products = [i for i in existing_products if i]
        file.close()

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in ', '.join(existing_products):
                    file.write(f'{product.name}, {product.weight}, {product.category}\n')
                else:
                    print(f'Продукт {product.name} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

