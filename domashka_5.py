from Hello import Hello

class NewClass(Hello):
    def __init__(self, name):
        super().__init__(name)

from class1 import NewClass
from tptin import tptint

# Создание объекта нового класса
obj = NewClass("Example")

# Применение функции к объекту
tptint(obj)
