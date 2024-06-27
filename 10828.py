import sys
# chatgpt helpd
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(int(num))

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return -1
    
    def size(self):
        return len(self.stack)

    def is_empty(self):
        return 0 if self.stack else 1

    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1

def main():
    n = int(sys.stdin.readline())
    stack = Stack()
    result = []

    for _ in range(n):
        command = sys.stdin.readline().split()

        if command[0] == "push":
            stack.push(command[1])
        elif command[0] == "pop":
            result.append(stack.pop())
        elif command[0] == "size":
            result.append(stack.size())
        elif command[0] == "empty":
            result.append(stack.is_empty())
        elif command[0] == "top":
            result.append(stack.top())

    for r in result:
        sys.stdout.write(str(r) + "\n")

if __name__ == '__main__':
    main()