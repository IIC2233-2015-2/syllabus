# coding=utf-8


class Node:

    def __init__(self, value, siguiente=None):
        self.value = value
        self.siguiente = siguiente


class Stack:

    def __init__(self):
        # Con lista: self.lista = []
        self.head = None

    def push(self, value):
        # Con lista: self.lista.append(value)
        if self.head:
            node = Node(value, self.head)
            self.head = node
        else:
            self.head = Node(value)

    def pop(self):
        # Con lista: return self.lista.pop()
        if self.head:
            temp = self.head
            self.head = self.head.siguiente
            return temp.value

    def top(self):
        # Con lista: return self.lista[-1]
        return self.head.value

    def __len__(self):
        # Con lista: return len(self.lista)
        temp, count = self.head, 0
        while temp:
            count += 1
            temp = temp.siguiente
        return count

    def __repr__(self):
        # return self.lista
        temp = self.head
        string = "Estado del {}: \n{}".format(self.__class__.__name__, '-'*20)
        while temp:
            string += '\n' + temp.value
            temp = temp.siguiente
        return string


class FixedStack(Stack):

    def __init__(self, capacidad):
        super().__init__(self)
        self.capacidad = capacidad

    def push(self, value):
        if not self.is_full:
            super().push(value)

    @property
    def is_full(self):
        return len(self) < self.capacidad


class StepStack(FixedStack):

    def __init__(self, siguiente=None, **kwargs):
        super().__init__(**kwargs)
        self.siguiente = siguiente

    def push(self, value):
        if self.is_full and self.siguiente:
            self.siguiente.push(value)
        elif self.is_full and not self.siguiente:
            self.siguiente = StepStack(capacidad=self.capacidad)
            self.siguiente.push(value)
        else:
            super().push(value)
