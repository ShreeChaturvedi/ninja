from math import log10, floor, isqrt

ones = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')

twos = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')

tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')

suffixes = ('', 'Thousand', 'Million', 'Billion')


def Roman(n: int):
    _values = [
        1000000, 900000, 500000, 400000, 100000, 90000, 50000, 40000, 10000, 9000, 5000, 4000, 1000, 900, 500, 400, 100,
        90, 50, 40, 10, 9, 5, 4, 1]

    _strings = [
        'M', 'C', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', "M", "CM", "D", "CD", "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"]

    result = ''
    decimal = n

    while decimal > 0:
        for i in range(len(_values)):
            if decimal >= _values[i]:
                if _values[i] > 1000:
                    result += u'\u0304'.join(list(_strings[i])) + u'\u0304'
                else:
                    result += _strings[i]
                decimal -= _values[i]
                break
    return result


def Base(n: int, b: int, b0=10):
    n = int(n, b0)
    num_rep = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K',
               21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V',
               32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}
    st_num = ''
    c = n
    while c != 0:
        rem = c % b
        if 36 > rem > 9:
            remainder_string = num_rep[rem]
        elif rem >= 36:
            remainder_string = '(' + str(rem) + ')'
        else:
            remainder_string = str(rem)
        st_num = remainder_string + st_num
        c = c // b
    return st_num


def process(n, index):
    if n == '0':
        return 'Zero'

    length = len(n)

    if length > 3:
        return False

    n = n.zfill(3)
    words = ''

    h_digit = int(n[0])
    t_digit = int(n[1])
    o_digit = int(n[2])

    words += '' if n[0] == '0' else ones[h_digit]
    words += ' Hundred ' if not words == '' else ''

    if t_digit > 1:
        words += tens[t_digit - 2]
        words += ' '
        words += ones[o_digit]

    elif t_digit == 1:
        words += twos[(int(t_digit + o_digit) % 10) - 1]

    elif t_digit == 0:
        words += ones[o_digit]

    if words.endswith('Zero'):
        words = words[:-len('Zero')]
    else:
        words += ' '

    if len(words) != 0:
        words += suffixes[index]

    return words


def Name(n: int):
    length = len(str(n))
    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []

    for i in range(length - 1, -1, -3):
        words.append(process(str(n)[0 if i - 2 < 0 else i - 2: i + 1], copy - count))
        count -= 1

    final_words = ''
    for s in reversed(words):
        temp = s + ' '
        final_words += temp
    return final_words


def Fibonacci(n: int):
    a, b = 0, 1
    if n < 0:
        return 'n<0'
    elif n < 2:
        return n
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return b


def Parity(n: int):
    if n % 2 == 0:
        return 'Even'
    return 'Odd'


def Tally(n: int):
    print('卌 ' * (n // 5) + '|' * (n % 5))


def NarcissisticQ(n: int):
    n_ = n
    length = floor(log10(n)) + 1
    s = 0
    for i in range(length):
        t = n
        n //= 10
        s += (t - n * 10) ** length
    return n_ == s


def PalindromeQ(n: int):
    return str(n) == str(n)[::-1]


def Visualise(n: int):
    o = '⬤ '
    for i in range(isqrt(n), 0, -1):
        if n % i == 0:
            print((o * int(n / i) + '\n') * i)
            return


def PrimeQ(n: int):
    if n < 2:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def PrimeFactors(n: int):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            factors.append(d)
        d += 1
    if n > 1:
        factors.append(n)
    uniques = list(set(factors))
    product = ''
    for factor in uniques:
        count = factors.count(factor)
        product += str(factor)
        if count > 1:
            product += '^' + str(count)
        product += ' × '
    return(product[:len(product) - 2])


def Prime(n: int):
    if n == 1:
        return 2
    count = 1
    num = 1
    while count < n:
        num += 2
        if PrimeQ(num):
            count += 1
    return num


def Primes(n: int):
    prime = [True in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return [i for i in range(2, n + 1) if prime[i]]
