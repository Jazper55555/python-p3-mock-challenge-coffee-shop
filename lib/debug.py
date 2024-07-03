#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

coffee = Coffee("Mocha")
customer = Customer('Wayne')
customer_2 = Customer('Dima')
order_1 = Order(customer, coffee, 2.0)
order_2 = Order(customer_2, coffee, 5.0)

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    ipdb.set_trace()
