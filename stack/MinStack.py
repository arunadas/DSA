# 155. Min Stack
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        current_min = self.stack[-1][-1]
        self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":
    obj = MinStack()
    obj.push(2)

    obj.push(7)
    print(obj)
    obj.push(1)
    print(obj)

