class MethodNotAllowed(Exception):
    pass

class Bike:
    def __init__(self, description, condition, sale_price, cost=0):         # Called using Bike()
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost

        self.sold = False
        self.id = None

    def update_sale_price(self, sale_price): # METHOD
        if self.sold:
            raise MethodNotAllowed("Can't update sale price on sold items")
        self.sale_price = sale_price

    def sell(self):
        self.sold = True
        profit = self.sale_price - self.cost
        return profit

    def service(self, cost=0, new_condition=None, new_sale_price=None):
        self.cost += cost
        if new_sale_price:
            self.update_sale_price(new_sale_price)
        if new_condition:
            self.condition = new_condition


if __name__ == '__main__':
    my_bike = Bike("2002 Raleigh", "Good", 200)
    print(my_bike)

    my_bike.service(cost=30, new_sale_price=300)
    my_bike.update_sale_price(100)
    my_bike.sell()