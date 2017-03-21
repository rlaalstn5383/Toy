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


if __name__ == '__main__':
    st = IntegerStack()
    st.push(1)
    st.push(2)
    st.push(3)

    print st.pop()
    print st.pop()
    print st.pop()
