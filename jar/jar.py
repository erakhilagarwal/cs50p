class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, cap):
        if int(cap) < 0:
            raise ValueError("Capacity of jar can not be less than ZER0")
        self._capacity = cap

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, si):
        if si < 0:
            raise ValueError("Do not have that many C🍪🍪KIES")
        if si > self.capacity:
            raise ValueError("Too many C🍪🍪KIES. Cannot hold")
        self._size = si
