#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount = 0, total = 0, items = None):
        self.discount = discount
        self.total = total        
        self.items = []


    @property
    def discount(self):
        return self._discount 

    @discount.setter
    def discount(self, discount):
        self._discount = discount

    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self, total):
        self._total = total

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    def add_item(self, item, price, quantity = 1):
        self._total += price*quantity
        self.last_amount = price
        self.last_quantity = quantity
        for i in range(0, quantity):
            self._items.append(item)

    def apply_discount(self):
        if self._discount:
            self._total = self._total - (self._total*self._discount/100) 
            print(f'After the discount, the total comes to ${round(self.total)}.')
        else:
            print("There is no discount to apply.")


    def reset_register_totals(self):
        self._total = 0
        self._items.clear()
        self._discount = 0

    def void_last_transaction(self):
        for i in range(0,self.last_quantity):
            self._total -= self.last_amount
            self._items.pop()
        if self._items == []:
            self._total == 0.0
        
