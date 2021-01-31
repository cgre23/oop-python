from enum import Enum


class MethodNotAllowed(Exception):
    pass


class Condition(Enum):
    NEW = 'new'
    GOOD = 'good'
    OKAY = 'ok'
    BAD = 'bad'


class Bike:
    num_wheels = 2
    counter = 0

    def __init__(self, description, condition, sale_price, cost=0):         # Called using Bike()
       # if not isinstance(condition, Condition):
       #     raise Exception('Expected Condition')

        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost
        Bike.counter += 1

        self.sold = False
        print("Bike created")

    def __del__(self):   # Gets called right before the object is deleted at the end of the process
        Bike.counter -= 1

    def update_sale_price(self, sale_price): # METHOD
        if self.sold:
            raise MethodNotAllowed("Can't update sale price on sold items")
        self.sale_price = sale_price

    def sell(self):
        self.sold = True
        profit = self.sale_price - self.cost
        return profit

    @property
    def profit(self):
        return self.sale_price - self.cost

    def service(self, cost=0, new_condition=None, new_sale_price=None):
        self.cost += cost
        if new_sale_price:
            self.update_sale_price(new_sale_price)
        if new_condition:
            self.condition = new_condition

    def __str__(self):
        return f"Bike: {self.description}"

    def __repr__(self):
        return f"Bike object: {self.description}, {self.condition.name}, sold={self.sold}"


class Tricycle(Bike):
    num_wheels = 3


if __name__ == '__main__':
    my_bike = Bike("2002 Raleigh", Condition.GOOD, 200)
    assert Bike.counter == 1
    bike_2 = Tricycle("tri 2", Condition.BAD, 300)
    print(my_bike.num_wheels)
    print(bike_2.num_wheels)

    my_bike.service(cost=30, new_sale_price=300)
    my_bike.update_sale_price(100)
    my_bike.sell()
    print(my_bike.profit)

