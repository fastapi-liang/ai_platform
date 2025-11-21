import os

class A:
    def __init__(self):
        self.a=1
        self.path = os.getcwd()
    def print(self):
        print(self.a)
a=1
print(a)
print("hello world")