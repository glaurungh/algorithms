# Задание Stepic:
# https://stepik.org/lesson/41234/step/4?unit=19818
# Стек с поддержкой максимума
# Реализовать стек с поддержкой операций push, pop и max.
# Вход. Последовательность запросов push, pop и max.
# Выход. Для каждого запроса max вывести максимальное число, находящееся на стеке.
# Формат входа. Первая строка содержит число запросов q. 
# Каждая из последующих q строк задаёт запрос в одном из следующих форматов: push v, pop, or max.
# Формат выхода. Для каждого запроса max выведите (в отдельной строке) текущий максимум на стеке.

import sys

class MaxStack:
    _stack = []
    _maxitems = []
    _max = float("-inf")

    def __init__(self):
        self._stack = []
        self._maxitems = []
        self._max = float("-inf")

    def push(self, item):
        if self._stack:
            self._stack.append(item)
            if item > self._max:
                self._max = item
            self._maxitems.append(self._max)
        else:
            self._stack.append(item)
            self._maxitems.append(item)
            self._max = item
    
    def pop(self):
        item = self._stack.pop()
        _ = self._maxitems.pop()
        self._max = self._maxitems[-1]
        return item

    def max(self):
        return self._max

n = int(input())

stack = MaxStack()

for i in range(n):
    command = sys.stdin.readline()
    if command.startswith("push"):
        _, number = list(command.split())
        stack.push(int(number))
    elif command.startswith("pop"):
        stack.pop()
    elif command.startswith("max"):
        print(stack.max())
