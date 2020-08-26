from utilities import *
from math import nan
STEP = 0.1
TOL = 1e-10
CYCLES = 1000


def Roots(f, r=100):
    ests = float_range(-r, r, STEP)
    roots = [Secant(f, est, r) for est in ests]
    x = ', '.join(Symbolics(Uniques([ToNumber(round(root, 4)) for root in roots if isfinite(root)]), 4))
    StdOut('x={' + x + '}')
    StdOut(f'{-r} < x < {r}')


def Secant(f, x, r, tol=TOL, cycles=CYCLES, step=STEP):
    x0 = x - step
    x1 = x + step
    fx0, fx1 = F(f, [x0]), F(f, [x1])
    if isnan(fx0) or isnan(fx1):
        return nan
    x2 = x0 - (x1 - x0) * fx0 / (fx1 - fx0)
    for i in range(cycles):
        x0, x1 = x1, x2
        fx0, fx1, fx2 = F(f, [x0]), F(f, [x1]), F(f, [x2])
        if abs(x2) > r:
            return nan
        if x0 == x1 or abs(fx2) < tol:
            return x2
        if fx0 == fx1:
            return nan
        x2 = x0 - (x1 - x0) * fx0 / (fx1 - fx0)
    return x2


def SumOfRoots(polynomial):
    terms = Terms(polynomial)
    i_c = {k: v for v, k in StdPoly(terms)}
    degree = max(i_c)
    a = i_c[degree]
    b = i_c.get(degree - 1, 0)
    return ToNumber(-b / a)


def ProductOfRoots(polynomial):
    terms = Terms(polynomial)
    i_c = {k: v for v, k in StdPoly(terms)}
    degree = max(i_c)
    a = i_c[degree]
    b = i_c.get(0, 0)
    return ToNumber((-1) ** degree * b / a)


def Degree(poly):
    terms = Terms(poly)
    return ToNumber(max([Index(term) for term in terms]))


def Lead(poly):
    terms = Terms(poly)
    lead = Index(terms[0])
    lead_term = terms[0]
    for term in terms:
        i = Index(term)
        if i > lead:
            lead = i
            lead_term = term
    return lead_term
