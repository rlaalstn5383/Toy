def parse(S):
    S = S.replace(" ", "")
    if len(S) == 0:
        raise Exception("Bad syntax" + S)
    cnt = 0
    for i in S:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            raise Exception("Bad syntax" + S)
    if cnt != 0:
        raise Exception("Bad syntax" + S)
    if S[0] != '(':
        return S
    S = S[1 :]
    ret = []
    pos = 0
    for i in range(len(S)):
        if S[i] == '(':
            cnt += 1
        elif S[i] == ')':
            cnt -= 1
        if cnt == 0:
            ret.append(parse(S[pos : i + 1]))
            pos = i + 1
    return tuple(ret)


class AE(object):
    def __init__(self):
        pass

    def eval(self):
        pass
