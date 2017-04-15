from collections import namedtuple


class Entry(object):
    def __str__(self):
        return '\n'.join(self.string())

    def __repr__(self):
        return 'Entry()'

    def string(self):
        return NotImplemented

class NoneEntry(Entry):
    def __repr__(self):
        return 'NoneEntry()'

class TreeEntry(Entry):
    def __init__(self, value):
        self.__left = NoneEntry()
        self.__right = NoneEntry()
        self.__value = value

    def __repr__(self):
        return 'TreeEntry(%s)' %self.value()

    def string(self):
        result = [str(self.value())]
        try:
            left_string = ['|    %s' %string for string in self.left().string()]
            left_string[0] = '|___ ' + left_string[0][5:]
            result += left_string
        except AssertionError:
            pass
        try:
            right_string = ['     %s' %string for string in self.right().string()]
            right_string[0] = '|___ ' + right_string[0][5:]
            result += ['|'] + right_string
        except AssertionError:
            pass
        return result

    def left(self, entry=None):
        if isinstance(entry, Entry):
            self.__left = entry
            return self

        assert not isinstance(self.__left, NoneEntry)

        return self.__left

    def right(self, entry=None):
        if isinstance(entry, Entry):
            self.__right = entry
            return self

        assert not isinstance(self.__right, NoneEntry)

        return self.__right

    def value(self, v=None):
        if v is None:
            return self.__value

        self.__value = v
        return self

class Tree(object):
    def __init__(self, root=NoneEntry()):
        self.__root = root

    def __str__(self):
        return str(self.root())

    def root(self, entry=None):
        if isinstance(entry, Entry):
            self.__root = entry
            return self

        assert not isinstance(self.__root, NoneEntry)

        return self.__root

    def preorder(self):
        stack = [self.root()]
        result = ''

        while stack:
            cur = stack.pop()
            try:
                stack.append(cur.right())
            except AssertionError:
                pass
            try:
                stack.append(cur.left())
            except AssertionError:
                pass
            result += '%s ' %cur.value()

        return result

    def postorder(self):
        FunctionCall = namedtuple('FunctionCall', ['entry', 'status'])
        stack = [FunctionCall(entry=self.root(), status=0)]
        result = ''

        while stack:
            cur = stack.pop()
            if cur.status == 0:
                stack.append(FunctionCall(entry=cur.entry, status=1))
                try:
                    stack.append(FunctionCall(entry=cur.entry.right(), status=0))
                except AssertionError:
                    pass
                try:
                    stack.append(FunctionCall(entry=cur.entry.left(), status=0))
                except AssertionError:
                    pass
            else:
                result += '%s ' %cur.entry.value()

        return result

if __name__ == '__main__':
    tree = Tree(TreeEntry('A').left(TreeEntry('B').left(TreeEntry('D') \
            .left(TreeEntry('H')).right(TreeEntry('I'))).right(TreeEntry('E'))) \
            .right(TreeEntry('C').left(TreeEntry('F')).right(TreeEntry('G'))))
    print(tree)
    print('preorder traversal: %s' %tree.preorder())
    print('postorder traversal: %s' %tree.postorder())

