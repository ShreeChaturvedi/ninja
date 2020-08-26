from math import *
from decimal import *
from colorama import Fore
from inspect import getsourcelines
from fractions import Fraction

ENGLISH_IDENTIFIERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', '𝑥', 'y', '𝒚', 'z']

GREEK_IDENTIFIERS = ['α', 'β', 'γ', 'η', 'θ', 'ι', 'κ', 'λ', 'ν', 'ο', '𝜋', 'ρ', 'φ', 'χ', 'ψ', 'ω']

RECOGNIZED_IDENTIFIERS = ENGLISH_IDENTIFIERS + GREEK_IDENTIFIERS

PHI = (1 + sqrt(5)) / 2

powers = {'1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '0': '⁰', '.': '˙',
          '+': '⁺', '-': '⁻', '/': 'ᶦ', '^': '^', '(': '⁽', ')': '⁾', "a": "ᵃ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ", "e": "ᵉ",
          "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ͥ ", "j": "ʲ", "k": "ᵏ", "l": "ˡ", "m": "ᵐ", "n": "ⁿ", "o": "ᵒ", "p": "ᵖ",
          "q": "۹", "r": "ʳ", "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ", "y": "ʸ", "z": "ᶻ", ' ': ''}

STD_FUNCTIONS = ('arcsinh', 'arccosh', 'arctanh', 'arcsin', 'arccos', 'arctan', 'sinh', 'cosh', 'tanh', 'sin',
                 'cos', 'tan', '√')

constants = {pi: '𝜋', e: 'e', PHI: 'φ'}


def Coefficient(term):
    current_coefficient = ''
    for char in term:
        if char not in '-0123456789.':
            break
        current_coefficient += char
    return UnNormalize(current_coefficient)


def Coefficients(terms):
    return [Coefficient(term) for term in terms]


def NonCoefficient(term):
    for char in term:
        if char in RECOGNIZED_IDENTIFIERS:
            return term[term.find(char):]
    return ''


def Index(term):
    if 'x' not in term:
        return 0
    index = UnNormalize(term[term.find('x') + 1:])
    if '/' in term:
        index *= -1
    return index


def StdPoly(terms):
    return sorted([(Coefficient(term), Index(term)) for term in terms])


def ToNumber(s):
    n = float(s)
    if n.is_integer():
        return int(n)
    return n


def Sqrt(n):
    root = int(sqrt(n))
    for factor_root in range(root, 1, -1):
        factor = factor_root * factor_root
        if n % factor == 0:
            reduced = n // factor
            if reduced == 1:
                return f'{ToNumber(factor_root)}'
            return f'{ToNumber(factor_root)}√{ToNumber(reduced)}'
    return f'√{ToNumber(n)}'


def Normalize(n):
    if n == 1:
        return ''
    elif n == -1:
        return '-'
    return str(n)


def UnNormalize(n):
    if n == '':
        return 1
    elif n == '-':
        return -1
    else:
        return float(n)


def ToComplexNumber(n: complex):
    return complex(ToNumber(n.real), ToNumber(n.imag))


def ComplexMax(x: complex, y: complex):
    if x.real > y.real:
        return x
    elif y.real > x.real:
        return y
    if x.imag > y.imag:
        return x
    else:
        return y


def ComplexMin(x: complex, y: complex):
    if x.real < y.real:
        return x
    elif y.real < x.real:
        return y
    if x.imag < y.imag:
        return x
    else:
        return y


def ComplexRound(n: complex, p):
    return complex(round(n.real, p), round(n.imag, p))


def ReducedFraction(x, y):
    n = Fraction(x, y)
    if n.denominator == 1:
        return n.numerator
    return f'{n.numerator}/{n.denominator}'


def Sign(n):
    try:
        if n < 0:
            return '-'
        return '+'
    except:
        return '+'


def ToNumbers(strings):
    return [ToNumber(string) for string in strings]


def Symbolic(n: float, p: int):
    if n == 0:
        return '0'
    for c in constants.keys():
        k = round(c, p)
        if abs(n) > abs(k):
            quotient = round(n / c, p)
            if quotient == round(quotient, round(p / 2)):
                return f'{Normalize(ToNumber(quotient))}{constants[c]}≈{n}'
        elif abs(n) < abs(k):
            quotient = round(c / n, p)
            if quotient.is_integer():
                sign = '-' if quotient < 0 else ''
                return f'{sign}{constants[c]}/{ToNumber(abs(quotient))}≈{n}'
        else:
            sign = '-' if n < 0 else ''
            return f'{sign}{constants[c]}≈{n}'
    return str(n)


def Symbolics(ns: list, p: int):
    return [Symbolic(n, p) for n in ns]


def group_terms(terms):
    group = []
    temp = terms.copy()
    while len(temp) != 0:
        current_group = []
        search = NonCoefficient(temp[0])
        for term in terms:
            if search == NonCoefficient(term):
                current_group.append(term)
                temp.remove(term)
        group.append(current_group)
    return group


def MultiplySymbols(terms):
    found_symbols = {}
    result = ''
    for term in terms:
        for i, c in enumerate(term):
            if c in RECOGNIZED_IDENTIFIERS:
                if c in found_symbols:
                    found_symbols[c] += float(Coefficient(term[i + 1:]))
                else:
                    found_symbols[c] = float(Coefficient(term[i + 1:]))
    for k, v in sorted(found_symbols.items()):
        result += '*' + k
        if v != 1:
            result += '**' + str(ToNumber(v))
    return result


def Terms(polynomial):
    terms = polynomial.replace('-', '+-').split('+')
    if '' in terms:
        terms.remove('')
    return terms


def CombineTerms(terms):
    return '+'.join(terms).replace('+-', '-')


def Uniques(items):
    return sorted(list(set(items)))


def Sorted(items):
    item_pairs = {k: v for k, v in zip(Coefficients(items), items)}
    coefficients = item_pairs.keys()
    return [item_pairs[item] for item in sorted(coefficients)]


def F(f, var, n=nan, r=4, is_round=False):
    try:
        if is_round:
            return round(f(*var), r)
        return f(*var)
    except:
        return n


def Var(f):
    lambda_f = getsourcelines(f)[0][0].strip('\n')
    return lambda_f[lambda_f.find(':') - 1]


def float_range(start, stop, step):
    while start < stop:
        yield float(start)
        start += Decimal(step)


def round_complex(num):
    return complex(round(num.real), round(num.imag))


def LambdaNotation(f):
    lambda_f = getsourcelines(f)[0][0].strip('\n')
    return lambda_f[lambda_f.find(':') + 1:]


def MathNotation(expression):
    math_symbols = [('**', '^'), ('+', ' + '), ('-', ' - '), ('*', ' '), ('/', ' / '), ('=', ' = '), ('∈', ' ∈ '),
                    ('±', ' ± '), ('≈', ' ≈ '), ('sqrt', '√'), ('asin', 'arcsin'), ('acos', 'arccos'),
                    ('atan', 'arctan'), ('  ', ' ')]

    for math_symbol in math_symbols:
        expression = expression.replace(math_symbol[0], math_symbol[1])

    new = ''
    is_power = False
    is_parenthesis = False
    parenthesis = 0

    for i, c in enumerate(expression):

        if c == '^' and not is_power:
            is_power = True
            if expression[i + 1] == '(':
                is_parenthesis = True
                parenthesis = 0
            else:
                is_parenthesis = False
            continue

        if c == '(':
            parenthesis += 1
            if is_power and is_parenthesis and parenthesis == 1:
                continue
        elif c == ')':
            parenthesis -= 1

        if is_power:
            if not (is_parenthesis or c in '.0123456789'):
                is_power = False
            elif is_parenthesis and parenthesis == 0:
                is_power = False
                continue

        if is_power:
            new += powers[c]
        else:
            new += c

    return new.replace('(x)', 'x').replace('⁽ˣ⁾', 'ˣ').replace('x', '𝑥').replace('y', '𝒚')


def color_out(output, n='\n'):
    for function in STD_FUNCTIONS:
        output = output.replace(function, "'" + function + '"')
    parenthesis = 0
    for c in output:
        if c in RECOGNIZED_IDENTIFIERS:
            print(Fore.CYAN, end='')
        elif c in powers.values():
            print(Fore.RED, end='')
        else:
            print(Fore.RESET, end='')

        if c == "'":
            parenthesis += 1
            continue
        elif c == '"':
            parenthesis -= 1
            continue
        if parenthesis > 0:
            is_function = True
        else:
            is_function = False
        if is_function:
            print(Fore.YELLOW, end='')
        print(c, end='')
    print(end=n)


def StdOut(expression, n='\n'):
    color_out(MathNotation(expression).strip(), n=n)


def Text(out, n='\n'):
    print(Fore.YELLOW + out, end=n)
