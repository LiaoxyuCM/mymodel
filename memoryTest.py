class tinyIO:
    def __init__(self):
        self.value = "";self.log = [];
    def write(self, val: str = ""):
        self.value = self.value+val;self.log.append(self.value);
    def reWrite(self, val: str = ""):
        self.value = val;self.log.append(self.value);
    def backspace(self):
        self.value = self.value[:-1];self.log.append(self.value);
    def remove(self):
        self.value = "";self.log.append(self.value);
    def newLine(self):
        self.value = self.value+"\n";self.log.append(self.value);
    def undo(self):
        if len(self.log) > 1:
            self.log.pop();self.value = self.log[-1];
        elif len(self.log) == 1:
            self.log.pop();self.value = "";
    def readALine(self, val: int = 1) -> str:
        _list = self.value.split("\n");return _list[val-1];
    def readAll(self) -> str:
        return self.value;

class stackMemory:
    def __init__(self) -> None:
        self.stack = []
    def write(self, val):
        self.stack.append(val)
    def delete(self):
        self.stack.pop()
    def read(self):
        return self.stack[len(self.stack)-1]
    def clear(self):
        self.stack = []

