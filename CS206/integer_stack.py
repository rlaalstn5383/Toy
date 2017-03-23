class Stack(object):
    def __init__(self):
        self.__top = EmptyEntry()

    def push(self, entry):
        assert isinstance(entry, OneEntry)

        entry.set_next(self.__top)
        self.__top = entry

    def pop(self):
        assert not isinstance(self.__top, EmptyEntry)

        ret = self.__top
        self.__top = self.__top.next()

        return ret

    def top(self):
        return self.__top

    def empty(self):
        return isinstance(self.top, EmptyEntry)

class IntegerStack(Stack):
    def __init__(self):
        self.__stack = Stack()
        super(IntegerStack, self).__init__()

    def push(self, num):
        assert isinstance(num, int)

        entry = IntegerEntry(num)
        super(IntegerStack, self).push(entry)

    def pop(self):
        entry = super(IntegerStack, self).pop()
        return int(entry)

    def top(self):
        entry = super(IntegerStack, self).top()
        return int(entry)

class Entry(object):
    pass

class EmptyEntry(Entry):
    pass

class NoneEntry(Entry):
    pass

class OneEntry(Entry):
    def __init__(self):
        self.__next = NoneEntry()

    def next(self):
        assert not isinstance(self.__next, NoneEntry)

        return self.__next

    def set_next(self, entry):
        assert isinstance(entry, Entry)

        self.__next = entry

class IntegerEntry(OneEntry):
    def __init__(self, value):
        assert isinstance(value, int)

        self.__value = value
        super(IntegerEntry, self).__init__()

    def __int__(self):
        return self.value()

    def value(self):
        return self.__value

def evaluate(eval_string):
    numstack = IntegerStack()
    opstack = IntegerStack()

    ADD = 1000001
    SUB = 1000002
    MUL = 1000003
    DIV = 1000004
    LEFT = 1000005
    RIGHT = 1000006

    def is_op(cur):
        curop = eval_string[cur]
        return curop == '+' or curop == '-' or curop == '*' or curop == '/' or curop == '(' or curop == ')'

    def is_right(cur):
        return eval_string[cur] == ')'

    def is_left(cur):
        return eval_string[cur] == '('

    def read_number(cur):
        ret = 0
        curr = cur
        if is_left(curr):
            return read_clause(curr)
        while not is_op(curr):
            ret *= 10
            ret += int(eval_string[curr])
            curr += 1
        numstack.push(ret)
        return curr

    def read_clause(cur):
        curr = cur
        numstack.push(LEFT)
        while not is_right(curr):
            curr += 1
            curr = read_number(curr)
            if eval_string[curr] == '+':
                opstack.push(ADD)
            elif eval_string[curr] == '-':
                opstack.push(SUB)
            elif eval_string[curr] == '*':
                curr = read_number(curr + 1)
                numstack.push(numstack.pop() * numstack.pop())
            elif eval_string[curr] == '/':
                curr = read_number(curr + 1)
                numstack.push(1 / numstack.pop() * numstack.pop())

        ret = numstack.pop()
        cur_number = numstack.pop()
        while not cur_number == LEFT:
            cur_op = opstack.pop()
            if cur_op == ADD:
                ret += cur_number
            elif cur_op == SUB:
                ret -= cur_number
            else:
                raise ValueError
            cur_number = numstack.pop()

        numstack.push(ret)

        curr += 1
        return curr

    eval_string = '(%s)' %eval_string
    read_number(0)

    return numstack.pop()







if __name__ == '__main__':
    st1 = '1+2'
    st2 = '1+(2+3)'
    st3 = '1*(1+2/3)'

    for st in (st1, st2, st3):
        print '%s = %d (%d)' %(st, evaluate(st), eval(st))
