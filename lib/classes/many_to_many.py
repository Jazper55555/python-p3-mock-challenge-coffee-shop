class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            raise Exception('Name cannot change once coffee is instantiated')
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception('Name must be a string more than 3 characters')

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in Order.all if order.coffee == self]))
    
    def num_orders(self):
        count = 0
        for coffee in Order.all:
            if coffee.coffee == self:
                count += 1
        return count
    
    def average_price(self):
        orders = [order.price for order in Order.all if order.coffee == self]
        return sum(orders) / len(orders)

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception('Name must be a string between 1 & 15 characters long')
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in Order.all if order.customer == self]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        all_customers = [order.customer for order in Order.all if order.coffee == coffee]
        if not all_customers:
            return None
        else:
            return max(all_customers, key=lambda customer: sum(order.price for order in customer.orders() if order.coffee == coffee))
            
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr(self, 'price'):
            raise Exception('Price cannot change once order is instantiated')
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise Exception('Price must be a float between 1.0 & 10.0')
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception('customer must be an instance of Customer')
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception('coffee must be an instance of Coffee')