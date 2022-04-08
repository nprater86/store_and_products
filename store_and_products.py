from Products import Product
from Store import Store

marianos = Store("Mariano's")

frozen_meatballs = Product("Frozen Meatballs",9.99,"Frozen Dinner")
frozen_pizza = Product("Frozen Pizza",16.99, "Frozen Dinner")
apple = Product("Apple",0.50,"Fruit")
banana = Product("Banana",0.60,"Fruit")
broccoli = Product("Broccoli",2.00,"Vegetable")

marianos.add_product(frozen_meatballs).add_product(frozen_pizza).add_product(apple).add_product(banana).add_product(broccoli)

frozen_meatballs.print_info()

marianos.check_inventory().inflation(0.05).check_inventory().sell_product(4).check_inventory()