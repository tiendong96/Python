class Product:
    def __init__(self, price) -> None:
        self.price = price 

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

product = Product(-10)
print(product.price)

#java learning python writes this , BUT 
#properties is an object that sits in front of an attribute and allows us to get or set the value of that attribute