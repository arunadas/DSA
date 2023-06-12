"""
Python Data Structures - Stack class
"""


class Stack:

    def __init__(self):
        self.item = []

    def is_empty(self):
        # return len(self.item) == 0
        return not self.item

    def push(self, element):
        self.item.append(element)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)


if __name__ == '__main__':
    s = Stack()
    s.push(7)
    print(s.size())
    s.push(6)
    s.push(0)
    print(s)
    print(s.peek())
    print(s.size())
    print(s.pop())
    print(s.is_empty())
