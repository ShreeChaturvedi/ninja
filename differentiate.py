class Polynomial:
    def __init__(self, top, btm):
        s = p_Euclid(top, btm)
        self.top, r = p_divide(top, s, [])
        self.btm, r = p_divide(btm, s, [])
        tp = self.top
        bt = self.btm
        t = []
        b = []
        for i in tp:
            if type(i) == tuple:
                t.append(i[0])
                b.append(i[1])
            else:
                t.append(i)
        for i in bt:
            if type(i) == tuple:
                t.append(i[0])
                b.append(i[1])
            else:
                t.append(i)
        if len(t) == 0:
            gcd = 1
        elif len(t) == 1:
            gcd = t[0]
        else:
            gcd = Euclid(t[0], t[1])
            for i in range(2, len(t)):
                gcd = Euclid(gcd, t[i])
        b += [1, 1]
        lcm = b[0] * b[1] // Euclid(b[0], b[1])
        for i in range(2, len(b)):
            lcm = lcm * b[i] // Euclid(lcm, b[i])
        for i in range(len(self.top)):
            if type(self.top[i]) == int:
                self.top[i] *= lcm
            else:
                self.top[i] = self.top[i][0] * lcm // self.top[i][1]
            self.top[i] //= gcd
        for i in range(len(self.btm)):
            if type(self.btm[i]) == int:
                self.btm[i] *= lcm
            else:
                self.btm[i] = self.btm[i][0] * lcm // self.btm[i][1]
            self.btm[i] //= gcd

    def derive(self):
        top = self.top
        btm = self.btm
        d1 = der(top)
        d2 = der(btm)
        return Polynomial(p_sub(p_multiply(d1, btm), p_multiply(d2, top)), p_multiply(btm, btm))

    def ptf(self):
        line = ''
        q = 0
        for i in range(len(self.top) - 1, 1, -1):
            if self.top[i] != 0:
                line += string(self.top[i]) + 'x^' + str(i) + '+'
                q += 1
        if len(self.top) >= 2 and self.top[1] != 0:
            line += string(self.top[1]) + 'x+'
            q += 1
        if self.top[0] != 0:
            line += str(self.top[0]) + '+'
            q += 1
        if q > 0:
            line = line[:-1]
        line2 = ''
        r = 0
        for i in range(len(self.btm) - 1, 1, -1):
            if self.btm[i] != 0:
                line2 += string(self.btm[i]) + 'x^' + str(i) + '+'
                r += 1
        if len(self.btm) >= 2 and self.btm[1] != 0:
            line2 += string(self.btm[1]) + 'x+'
            r += 1
        if self.btm[0] != 0:
            line2 += str(self.btm[0]) + '+'
            r += 1
        if r > 0:
            line2 = line2[:-1]
        if q == 0:
            return '0'
        elif line2 == '1':
            return line
        if q > 1:
            line = '(' + line + ')'
        if r > 1:
            line2 = '(' + line2 + ')'
        return line + '/' + line2


def string(x):
    odds = [1, -1]
    if x not in odds:
        return str(x)
    return str(x)[:-1]


def der(a):
    if len(a) > 1:
        return [fr_mult(a[i], i) for i in range(1, len(a))]
    else:
        return [0]


class trig:
    def __init__(self, name, arg):
        self.arg = count(parse(arg))
        self.name = name

    def derive(self):
        name = self.name
        arg = self.arg
        if name == 'sin':
            return multiply(arg.derive(), trig('cos', arg))
        elif name == 'cos':
            return sub(Polynomial([0], [1]), multiply(arg.derive(), trig('sin', arg)))
        elif name == 'tan':
            return divide(arg.derive(), power(trig('cos', arg), Polynomial([2], [1])))
        elif name == 'cot':
            return sub(Polynomial([0], [1]), divide(arg.derive(), power(trig('sin', arg), Polynomial([2], [1]))))

    def ptf(self):
        return self.name + '(' + self.arg.ptf() + ')'


class log:
    def __init__(self, base, arg):
        global F
        self.base = count(parse(base))
        self.arg = count(parse(arg))
        if eq(self.base, Polynomial([0], [1])):
            F = False
            print('Error: cannot take logarithm with base 0')
            return
        if type(self.arg) == Polynomial and len(self.arg.top) == 1 and len(self.arg.btm) == 1:
            if self.arg.top[0] < 0:
                F = False
                print('Error: cannot take logarithm of negative number')
                return
            elif self.arg.top[0] == 0:
                F = False
                print('Error: cannot take logarithm of 0')
                return

    def derive(self):
        base = self.base
        arg = self.arg
        return divide(arg.derive(), multiply(arg, ln(base)))

    def ptf(self):
        base = self.base
        arg = self.arg
        return 'log' + base.ptf() + '(' + arg.ptf() + ')'


class ln:
    def __init__(self, arg):
        global F
        self.arg = count(parse(arg))
        if type(self.arg) == Polynomial and len(self.arg.top) == 1 and len(self.arg.btm) == 1:
            if self.arg.top[0] < 0:
                F = False
                print('Error: cannot take logarithm of negative number')
                return
            elif self.arg.top[0] == 0:
                F = False
                print('Error: cannot take logarithm of 0')
                return

    def derive(self):
        arg = self.arg
        return divide(arg.derive(), arg)

    def ptf(self):
        return 'ln(' + self.arg.ptf() + ')'


class power:
    def __init__(self, base, power):
        self.base = count(parse(base))
        self.power = count(parse(power))

    def derive(self):
        base = self.base
        pw = self.power
        return add(multiply(multiply(power_f(base, pw), ln(base)), pw.derive()),
                   multiply(pw, multiply(power_f(base, sub(pw, Polynomial([1], [1]))), base.derive())))

    def ptf(self):
        base = self.base
        power = self.power
        if eq(power, Polynomial([1], [1])):
            return base.ptf()
        return '(' + base.ptf() + ')^(' + power.ptf() + ')'


class mixed_func:
    def __init__(self, f1, f2, mark):
        self.f1 = count(parse(f1))
        self.f2 = count(parse(f2))
        self.mark = mark

    def derive(self):
        f1 = self.f1
        f2 = self.f2
        mark = self.mark
        if mark == '+':
            return add(f1.derive(), f2.derive())
        elif mark == '-':
            return sub(f1.derive(), f2.derive())
        elif mark == '*':
            return add(multiply(f1, f2.derive()), multiply(f2, f1.derive()))
        return divide(sub(multiply(f2, f1.derive()), multiply(f1, f2.derive())), multiply(f2, f2))

    def ptf(self):
        mark = self.mark
        f1 = self.f1
        f2 = self.f2
        if mark == '+':
            return f1.ptf() + '+' + f2.ptf()
        elif mark == '-':
            if type(f2) == Polynomial and f2.btm == [1] and len(f2.top) > 1:
                line2 = '(' + f2.ptf() + ')'
            else:
                line2 = f2.ptf()
            return f1.ptf() + '-' + line2
        elif mark == '*':
            if (type(f1) == mixed_func and f1.mark in ['+', '-']) or (type(f1) == Polynomial and f1.btm == [1]):
                if type(f1) == mixed_func:
                    line = '(' + f1.ptf() + ')'
                else:
                    top = f1.top
                    q = 0
                    for i in top:
                        if i != 0:
                            q += 1
                    if q > 1:
                        line = '(' + f1.ptf() + ')'
                    else:
                        line = f1.ptf()
            else:
                line = f1.ptf()
            if (type(f2) == mixed_func and f2.mark in ['+', '-']) or (type(f2) == Polynomial and f2.btm == [1]):
                line2 = '(' + f2.ptf() + ')'
            else:
                line2 = f2.ptf()
            return line + '*' + line2
        if type(f1) == trig or type(f1) == ln or type(f1) == log or type(f1) == power or (
                type(f1) == mixed_func and f1.mark == '*'):
            line = f1.ptf()
        else:
            line = '(' + f1.ptf() + ')'
        return line + '/' + '(' + f2.ptf() + ')'


def power_f(base, pw):
    base1 = base
    power1 = pw
    b = count(parse(base))
    p = count(parse(pw))
    if type(p) == Polynomial:
        if p.top == [0]:
            return Polynomial([1], [1])
        elif p.top == [1] and p.btm == [1]:
            return b
    if type(b) == Polynomial and type(p) == Polynomial and len(p.top) == 1 and p.btm == [1] and p.top[0] > 0:
        result = b
        for i in range(1, p.top[0]):
            result = multiply(result, b)
        return result
    elif type(b) == power:
        b1 = b.base
        p1 = b.power
        return power(b1, multiply(p1, p))
    return power(base1, power1)


def p_Euclid(a1, b1):
    a = [i for i in a1]
    b = [i for i in b1]
    while b != [0]:
        res, mod = p_divide(a, b, [])
        a = [i for i in b]
        b = [i for i in mod]
    return a


def p_add(a, b):
    la = len(a)
    lb = len(b)
    l = max(la, lb)
    a1 = a + [0] * (l - la)
    b1 = b + [0] * (l - lb)
    res = [fr_add(a1[i], b1[i]) for i in range(l)]
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


def p_sub(a, b):
    return p_add(a, [fr_sub(0, b[i]) for i in range(len(b))])


def p_multiply(a, b):
    l = len(a) + len(b) - 1
    result = [0] * l
    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] = fr_add(fr_mult(a[i], b[j]), result[i + j])
    return result


def p_divide(a, b, result):
    if len(a) < len(b):
        if not result:
            result = [0]
        return result, a
    elif len(b) == 1:
        return [fr_div(i, b[0]) for i in a], [0]
    else:
        la = len(a)
        lb = len(b)
        if result == []:
            result = [0] * (la - lb + 1)
        curr = fr_div(a[-1], b[-1])
        curr_pos = la - lb
        new_res = [i for i in result]
        new_res[curr_pos] = curr
        s = [0] * (la - lb) + [fr_mult(b[i], curr) for i in range(lb)]
        return p_divide(p_sub(a, s), b, new_res)


def fraction(nm, dm):
    if nm != 0:
        gcf = Euclid(nm, dm)
        a = nm // gcf
        b = dm // gcf
        if b == 1:
            return a
        else:
            return (a, b)
    return 0


def Euclid(a, b):
    if b == 0:
        return a
    else:
        return Euclid(b, a % b)


def fr_mult(a1, b1):
    if type(a1) == int:
        a = (a1, 1)
    else:
        a = a1
    if type(b1) == int:
        b = (b1, 1)
    else:
        b = b1
    new_nm = a[0] * b[0]
    new_dm = a[1] * b[1]
    if new_nm != 0:
        k = Euclid(new_nm, new_dm)
        new_nm //= k
        new_dm //= k
    return fraction(new_nm, new_dm)


def fr_div(a, b1):
    if type(b1) == int:
        b = (b1, 1)
    else:
        b = b1
    return fr_mult(a, fraction(b[1], b[0]))


def fr_add(a1, b1):
    if type(a1) == int:
        a = (a1, 1)
    else:
        a = a1
    if type(b1) == int:
        b = (b1, 1)
    else:
        b = b1
    lcm = a[1] * b[1] // Euclid(a[1], b[1])
    return fraction(a[0] * lcm // a[1] + b[0] * lcm // b[1], lcm)


def fr_sub(a, b1):
    if type(b1) == int:
        b = (b1, 1)
    else:
        b = b1
    return fr_add(a, fraction(-b[0], b[1]))


def fr_ptf(a):
    if type(a) == int:
        return str(a)
    return str(a[0]) + '/' + str(a[1])


def count(func):
    if type(func) == mixed_func:
        mark = func.mark
        f1 = func.f1
        f2 = func.f2
        if mark == '+':
            return add(count(f1), count(f2))
        elif mark == '-':
            return sub(count(f1), count(f2))
        elif mark == '*':
            return multiply(count(f1), count(f2))
        return divide(count(f1), count(f2))
    elif type(func) == trig:
        return trig(func.name, count(func.arg))
    elif type(func) == log:
        return log(count(func.base), count(func.arg))
    elif type(func) == ln:
        return ln(count(func.arg))
    else:
        return func


def add(f1, f2):
    if type(f1) == Polynomial and f1.top == [0]:
        return f2
    elif type(f2) == Polynomial and f2.top == [0]:
        return f1
    elif type(f1) == type(f2) and type(f1) == Polynomial:
        p1 = f1
        p2 = f2
        s = p_Euclid(p1.btm, p2.btm)
        lcm, r = p_divide(p_multiply(p1.btm, p2.btm), s, [])
        s1, r = p_divide(p2.btm, s, [])
        s2, r = p_divide(p1.btm, s, [])
        return Polynomial(p_add(p_multiply(p1.top, s1), p_multiply(p2.top, s2)), lcm)
    elif eq(f1, f2):
        return multiply(Polynomial([2], [1]), f1)
    return mixed_func(f1, f2, '+')


def sub(f1, f2):
    if type(f2) == Polynomial and f2.top == [0]:
        return f1
    elif type(f1) == type(f2) and type(f1) == Polynomial:
        f3 = Polynomial([fr_sub(0, f2.top[i]) for i in range(len(f2.top))], f2.btm)
        return add(f1, f3)
    elif eq(f1, f2):
        return Polynomial([0], [1])
    return mixed_func(f1, f2, '-')


def multiply(f1, f2):
    if type(f1) == Polynomial:
        if f1.top == [0]:
            return Polynomial([0], [1])
        elif f1.top == [1] and f1.btm == [1]:
            return f2
        elif len(f1.top) == 1 and f1.top[0] < 0 and len(f1.btm) == 1:
            return sub(Polynomial([0], [1]), multiply(Polynomial([-f1.top[0]], f1.btm), f2))
    if type(f2) == Polynomial:
        if f2.top == [0]:
            return Polynomial([0], [1])
        elif f2.top == [1] and f2.btm == [1]:
            return f1
        elif len(f2.top) == 1 and f2.top[0] < 0 and len(f2.btm) == 1:
            return sub(Polynomial([0], [1]), multiply(Polynomial([-f2.top[0]], f2.btm), f1))
    if type(f1) == type(f2) and type(f1) == Polynomial:
        top = p_multiply(f1.top, f2.top)
        btm = p_multiply(f1.btm, f2.btm)
        s = p_Euclid(top, btm)
        top, r = p_divide(top, s, [])
        btm, r = p_divide(btm, s, [])
        return Polynomial(top, btm)
    if type(f2) == mixed_func and f2.mark == '/':
        return divide(multiply(f1, f2.f1), f2.f2)
    elif type(f1) == mixed_func and f1.mark == '/':
        return divide(multiply(f1.f1, f2), f1.f2)
    elif eq(f1, f2):
        return power(f1, '2')
    return mixed_func(f1, f2, '*')


def divide(f1, f2):
    global F
    if type(f2) == Polynomial:
        if f2.top == [0]:
            print('Error: division by zero')
            F = False
            return
        elif f2.top == [1] and f2.btm == [1]:
            return f1
    if type(f1) == Polynomial and f1.top == [0]:
        return Polynomial([0], [1])
    elif eq(f1, f2):
        return Polynomial([1], [1])
    elif type(f1) == type(f2):
        if type(f1) == Polynomial:
            return multiply(f1, Polynomial(f2.btm, f2.top))
        elif type(f1) == power and eq(f1.base, f2.base):
            return power(f1.base, sub(f1.power, f2.power))
        elif type(f1) == trig and eq(f1.arg, f2.arg):
            if f1.name == 'sin' and f2.name == 'cos':
                return trig('tan', f1.arg)
            elif f1.name == 'cos' and f2.name == 'sin':
                return trig('cot', f1.arg)
    if type(f2) == mixed_func and f2.mark == '/':
        return divide(multiply(f1, f2.f2), f2.f1)
    elif type(f1) == mixed_func and f1.mark == '/':
        return divide(f1.f1, multiply(f1.f2, f2))
    elif type(f1) == Polynomial and f1.btm != [1]:
        return divide(Polynomial(f1.top, [1]), multiply(Polynomial(f1.btm, [1]), f2))
    elif type(f2) == Polynomial and f2.btm != [1]:
        return divide(multiply(Polynomial(f2.btm, [1]), f1), Polynomial(f2.top, [1]))
    return mixed_func(f1, f2, '/')


def eq(f1, f2):
    if type(f1) == type(f2):
        t = type(f1)
        if t == Polynomial:
            if f1.top == f2.top and f1.btm == f2.btm:
                return True
            return False
        elif t == trig:
            if f1.name == f2.name and eq(f1.arg, f2.arg):
                return True
            return False
        elif t == log:
            if eq(f1.base, f2.base) and eq(f1.arg, f2.arg):
                return True
            return False
        elif t == ln:
            if eq(f1.arg, f2.arg):
                return True
            return False
        elif t == power:
            if eq(f1.base, f2.base) and eq(f1.power, f2.power):
                return True
            return False
        elif t == mixed_func:
            if f1.mark == f2.mark and ((eq(f1.f1, f2.f1) and eq(f1.f2, f2.f2)) or (
                    f1.mark in ['+', '*'] and (eq(f1.f2, f2.f1) and eq(f1.f1, f2.f2)))):
                return True
            return False
    return False


def parse(expression):
    global F
    if not F:
        return
    if type(expression) != str:
        return expression
    exp = ''.join(expression.split())
    if exp == '':
        F = False
        print('Syntax error: wrong format')
        return
    l = len(exp)
    marks1 = ['+', '-']
    digits = '1234567890'
    possible2 = '(xsctl'
    possible1 = digits + possible2
    trignames = ['sin', 'cos', 'tan', 'cot']
    checked = False
    while exp[0] == '(' and exp[-1] == ')' and not checked:
        balance = 1
        cnt = 0
        for i in range(1, l):
            if exp[i] == '(':
                balance += 1
            elif exp[i] == ')':
                balance -= 1
                if balance == 0:
                    cnt += 1
        if cnt == 1:
            exp = exp[1:l - 1]
            l -= 2
        else:
            checked = True
    balance = 0
    i = l - 1
    while i >= 0:
        if exp[i] == ')':
            balance += 1
        elif exp[i] == '(':
            balance -= 1
        elif exp[i] in marks1 and balance == 0:
            if i == 0:
                f = '0'
            else:
                f = exp[:i]
            return mixed_func(f, exp[i + 1:], exp[i])
        i -= 1
    i = 0
    balance = 0
    while i < l:
        if exp[i] == '(':
            balance += 1
        elif exp[i] == ')':
            balance -= 1
            if balance == 0 and i < l - 1 and exp[i + 1] in possible1:
                return mixed_func(exp[:i + 1], exp[i + 1:], '*')
        elif i > 0 and exp[i] == '*' and balance == 0:
            return mixed_func(exp[:i], exp[i + 1:], '*')
        elif exp[i] == 'x' and balance == 0 and i < l - 1 and exp[i + 1] in possible1:
            return mixed_func(exp[:i + 1], exp[i + 1:], '*')
        elif exp[i] in digits and balance == 0 and i < l - 1 and exp[i + 1] in possible2:
            k = i
            while i >= 0 and exp[i] in digits:
                i -= 1
            if i >= 0 and exp[i] == 'g':
                i = k
            else:
                return mixed_func(exp[:k + 1], exp[k + 1:], '*')
        i += 1
    i = 0
    balance = 0
    while i < l:
        if exp[i] == '(':
            balance += 1
        elif exp[i] == ')':
            balance -= 1
        elif exp[i] == '/' and balance == 0:
            return mixed_func(exp[:i], exp[i + 1:], '/')
        i += 1
    i = 0
    balance = 0
    while i < l:
        if exp[i] == '(':
            balance += 1
        elif exp[i] == ')':
            balance -= 1
            if balance == 0 and i < l - 2 and exp[i + 1] == '^':
                return power_f(exp[:i + 1], exp[i + 2:])
        elif i > 0 and exp[i] == '^' and i + 1 < l and balance == 0:
            return power_f(exp[:i], exp[i + 1:])
        i += 1
    if len(exp) > 3 and exp[:3] == 'log':
        i = 3
        while i < l and exp[i] in digits:
            i += 1
        if i == 3 or i == len(exp):
            F = False
            print('Syntax error: wrong format')
            return
        return log(exp[3:i], exp[i:])
    elif len(exp) >= 2 and exp[:2] == 'ln':
        return ln(exp[2:])
    elif len(exp) > 3 and exp[:3] in trignames:
        return trig(exp[:3], exp[3:])
    if exp == 'x':
        return Polynomial([0, 1], [1])
    else:
        flag = True
        for i in range(len(exp)):
            if exp[i] not in digits:
                flag = False
        if flag:
            return Polynomial([int(exp)], [1])
        else:
            print('Syntax error: wrong format')
            F = False
            return


def simplify(line):
    if line[0] == '+':
        return simplify(line[1:])
    signs = '+-'
    digits = '1234567890'
    for i in range(len(line)):
        if line[i] == '+' and line[i + 1] in signs:
            return simplify(line[:i] + line[i + 1:])
        if line[i] == '-' and i < len(line) - 1:
            if line[i + 1] == '-':
                return simplify(line[:i] + '+' + line[i + 2:])
            elif line[i + 1] == '+':
                return simplify(line[:i + 1] + line[i + 2:])
        if i < len(line) - 2 and line[i] == '(' and line[i + 2] == ')' and line[i + 1] in digits:
            k = i - 1
            while k >= 0 and line[k] in digits:
                k -= 1
            if not (k >= 0 and line[k] in 'stng'):
                return simplify(line[:i] + line[i + 1] + line[i + 3:])
        if line[i] == '0' and i < len(line) - 1 and line[i + 1] == '-':
            return simplify(line[:i] + line[i + 1:])
    return line


def D(exp):
    global F
    F = True
    f = count(parse(exp))
    if F:
        return simplify(count(f.derive()).ptf())
    return ''


def Dn(f, x, prec=1e-15):
    try:
        return (f(x + prec) - f(x - prec)) / prec
    except:
        return 'Undefined'
