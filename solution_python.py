class EventSourcer():
    # Do not change the signature of any functions
    def __init__(self):
        self.value = 0
        self.do_stack = []
        self.undo_stack = []

    def add(self, num: int):
        self.value += num
        self.do_stack.append(num)

    def subtract(self, num: int):
        num = -1*num
        self.value += num
        self.do_stack.append(num)

    def undo(self):
        if len(self.do_stack) != 0:
            num = self.do_stack.pop()
            self.value -= num
            self.undo_stack.append(num)

    def redo(self):
        if len(self.undo_stack) != 0:
            num = self.undo_stack.pop()
            self.value += num
            self.do_stack.append(num)

    def bulk_undo(self, steps: int):
        count = 0
        while count < steps and len(self.do_stack) != 0:
            num = self.do_stack.pop()
            self.value -= num
            self.undo_stack.append(num)
            count += 1

    def bulk_redo(self, steps: int):
        count = 0
        while count < steps and len(self.undo_stack) != 0:
            num = self.undo_stack.pop()
            self.value += num
            self.do_stack.append(num)
            count += 1
