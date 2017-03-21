import itertools

ALLOW_FIRST_0 = False
BRUTE_FORCE = False

def alphametic(lhs, rhs, carry, res, save, numbers):
    expr = [lhs, rhs, res]
    cnt = 0
    cnt2 = 0
    for i in (0, 1, 2):
        if len(expr[i]) == 0:
            expr[i] = '*'
            cnt2 += 1
        if expr[i][0] in save:
            cnt += 1
    lhs = expr[0]
    rhs = expr[1]
    res = expr[2]
    tnumbers = numbers[:]
    tsave = save.copy()

    if cnt2 == 3:
        if save[lhs[0]] + save[rhs[0]] + carry == save[res[0]]:
            return True, save
        return False, save
    if cnt == 3:
        if save[lhs[0]] + save[rhs[0]] + carry == save[res[0]]:
            return alphametic(lhs[1:], rhs[1:], 0, res[1:], save, numbers)
        elif save[lhs[0]] + save[rhs[0]] + carry - 10== save[res[0]]:
            return alphametic(lhs[1:], rhs[1:], 1, res[1:], save, numbers)
        else:
            return False, save
    elif cnt == 2:
        if res[0] in save:
            if lhs[0] in save:
                return alphametic(rhs, lhs, carry, res, save, numbers)
            if save[res[0]] - carry - save[rhs[0]] in numbers:
                save[lhs[0]] = save[res[0]] - carry - save[rhs[0]]
                if not ALLOW_FIRST_0:
                    if len(lhs) == 1 and save[lhs[0]] == 0:
                        return False, save
                numbers.remove(save[res[0]] - carry - save[rhs[0]])
                ret = alphametic(lhs[1:], rhs[1:], 0, res[1:], save, numbers)
                if ret[0]:
                    return ret
                numbers = tnumbers[:]
                save = tsave.copy()
            if save[res[0]] - carry - save[rhs[0]] + 10 in numbers:
                save[lhs[0]] = save[res[0]] - carry - save[rhs[0]] + 10
                if not ALLOW_FIRST_0:
                    if len(lhs) == 1 and save[lhs[0]] == 0:
                        return False, save
                numbers.remove(save[res[0]] - carry - save[rhs[0]] + 10)
                ret = alphametic(lhs[1:], rhs[1:], 1, res[1:], save, numbers)
                if ret[0]:
                    return ret
                numbers = tnumbers[:]
                save = tsave.copy()
            return False, save
        else:
            if save[lhs[0]] + save[rhs[0]] + carry >= 10:
                if save[lhs[0]] + save[rhs[0]] + carry - 10 in numbers:
                    save[res[0]] = save[lhs[0]] + save[rhs[0]] + carry - 10
                    if not ALLOW_FIRST_0:
                        if len(res) == 1 and save[res[0]] == 0:
                            return False, save
                    numbers.remove(save[lhs[0]] + save[rhs[0]] + carry - 10)
                    return alphametic(lhs[1:], rhs[1:], 1, res[1:], save, numbers)
                return False, save
            else:
                if save[lhs[0]] + save[rhs[0]] + carry in numbers:
                    save[res[0]] = save[lhs[0]] + save[rhs[0]] + carry
                    if not ALLOW_FIRST_0:
                        if len(res) == 1 and save[res[0]] == 0:
                            return False, save
                    numbers.remove(save[lhs[0]] + save[rhs[0]] + carry)
                    return alphametic(lhs[1:], rhs[1:], 0, res[1:], save, numbers)
                return False, save
    else:
        for e in expr:
            if not e[0] in save:
                break
        for i in tnumbers:
            save[e[0]] = i
            if not ALLOW_FIRST_0:
                if len(e) == 1 and save[e[0]] == 0:
                    continue
            numbers.remove(i)
            ret = alphametic(lhs, rhs, carry, res, save, numbers)
            if ret[0]:
                return ret
            numbers = tnumbers[:]
            save = tsave.copy()
        return False, save

def alphametic_brute(lhs, rhs, res):
    var = list(set(list(lhs + rhs + res)))
    for p in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], len(var)):
        save = {}
        for i in range(len(var)):
            save[var[i]] = p[i]
        if not ALLOW_FIRST_0:
            if save[lhs[0]] == 0:
                continue
            if save[rhs[0]] == 0:
                continue
            if save[res[0]] == 0:
                continue
        tlhs = lhs
        trhs = rhs
        tres = res
        for k in save:
            tlhs = tlhs.replace(k, str(save[k]))
            trhs = trhs.replace(k, str(save[k]))
            tres = tres.replace(k, str(save[k]))
        if int(tlhs) + int(trhs) == int(tres):
            save['*'] = 0
            return True, save
    return (False, )

def solve_alphametic(expr):
    texpr = expr
    expr = expr.split('=')
    if len(expr) != 2:
        raise
    expr[0] = expr[0].split('+')
    if len(expr[0]) != 2:
        raise
    lhs = expr[0][0].strip()
    rhs = expr[0][1].strip()
    res = expr[1].strip()
    save = {'*': 0}
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if BRUTE_FORCE:
        ret = alphametic_brute(lhs, rhs, res)
    else:
        ret = alphametic(lhs[::-1], rhs[::-1], 0, res[::-1], save, numbers)
    if ret[0]:
        ret[1].pop('*')
        for k in ret[1]:
            texpr = texpr.replace(k, str(ret[1][k]))
        return True, texpr, ret[1]
    else:
        return False


if __name__ == '__main__':
    BRUTE_FORCE = True
    print solve_alphametic('SINCE+JULIUS=CAESAR')
