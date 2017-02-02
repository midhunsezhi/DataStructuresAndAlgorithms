import sys

class Stack():
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.apend(item)

    def isEmpty(self):
        return len(self._data) == 0

    def pop(self):
        return self._data.pop()

    def top(self):
        return self._data[-1]
    
s = []
undo_stack = Stack()
q = int(sys.stdin.readline())
for _ in range(q):
    line = sys.stdin.readline()
    line = line.split(' ')
    type = int(line[0])
    if type == 1:
        value = line[1][:-1]
        undo_stack.push((type, len(value)))
        for char in value:
            s.append(char)
    elif type == 2:
        value = int(line[1])
        undo_stack.push((type, s[(-1 * value):]))
         s = s[:(-1 * value)]
    elif type == 3:
        value = int(line[1])
        undo_stack.push((type, value))
        print s[value-1]
    else:
        undo_op = undo_stack.pop()
        if undo_op[0] == 1: