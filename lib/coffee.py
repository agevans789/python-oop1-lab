#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

        @property
        def size(self):
            return self._size
        
        @size.setter
        def size(self, value):
            value = value.lower().strip()
            sizes = ["small", "medium", "large"]
            if value not in sizes:
                raise ValueError(f"size must be one of {sizes}.")
            self._size = value

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1