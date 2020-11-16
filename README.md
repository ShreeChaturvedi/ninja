# ninja
ninja aims to be a flexible and lightweight computer algebra system written purely in python. It provides several useful functions in pure mathematics, engineering and physics, and computer science.

## Capabilities
### Numbers:
- Check if an integer, n, is prime.<br>`Usage: PrimeQ(n: int)`
- Check if an integer, n, is a palindrome.<br>`Usage: PalindromeQ(n: float)`
- Check if an integer, n, is an armstrong.<br>`Usage: NarcissisticQ(n: int)`
- Check if an integer, n, is a perfect square.<br>`Usage: PerfectSquare(n: int)`
- Check if an integer, n, is a perfect cube.<br>`Usage: PerfectCube(n: int)`
- Check if an integer, n, is a perfect number.<br>`Usage: PerfectQ(n: int)`
- Check if an integer, n, is a deficient number.<br>`Usage: DeficientQ(n: int)`
- Check if an integer, n, is a abundant number.<br>`Usage: AbundantQ(n: int)`
- Return the n<sup>th</sup> prime number.<br>`Usage: Prime(n: int)`
- Return the n<sup>th</sup> tribonacci number with starting values `a` and `b`.<br>`Usage: Tribonacci(n: int, a: int, b: int)`
- Return the n<sup>th</sup> fibonacci number.<br>`Usage: Fibonacci(n: int)`
- Return the n<sup>th</sup> lucas number.<br>`Usage: Lucas(n: int)`
- Return the name of an integer, n, in words.<br>`Usage: Name(n: int)`
- Return the parity of an integer, n.<br>`Usage: Parity(n: int)`
- Return the representation of an integer, n, in Roman numerals.<br>`Usage: Roman(n: int)`
- Return the representation of an integer, n, in tally bars.<br>`Usage: Tally(n: int)`
- Return the visualization of a positive integer, n.<br>`Usage: Visualise(n: int)`
- Convert a number from any base, b0, to another base, b.<br>`Usage: Base(n, b, b0=10)`
- Return the continued fraction representation of a fraction, a / b.<br>`Usage: ContinuedFraction(a, b)`
- Return the GCD of a list of integers, n.<br>`Usage: GCD(n: list)`
- Return the LCM of a list of integers, n.<br>`Usage: LCM(n: list)`
- Return the one's complement of a binary string, n.<br>`Usage: OneComplement(n: str)`
- Return the two's complement of a binary string, n.<br>`Usage: TwoComplement(n: str)`
- Return the binary representation of a float, n, positive or negative with prec digits after decimal space.<br>`Usage: Binary(n: float, prec=10)`
- Return the Binary Coded Decimal (BCD) form of a float, n.<br>`Usage: BCD(n: float)`
- Return the Pascal's triangle with n rows.<br>`Usage: PascalTriangle(n: int)`
- Return the list of all factors of an integer, n.<br>`Usage: Factors(n: int)`
- Return the list of all prime factors of an integer, n.<br>`Usage: PrimeFactors(n: int)`
- Return the list of all prime numbers less than n; that is, in the range `0 < prime < n`.<br>`Usage: Primes(n: int)`
- Return a list of all the possible permutations of a list of items.<br>`Usage: Permutations(items: list)`
- Return the n<sup>th</sup> triangular number.<br>`Usage: Triangular(n: int)`
### Plotting
- Plot a list of several 2D functions, fs, in the range x0 < x < x1, with a precision of prec.<br>`Usage: Plot(fs, x0, x1, prec=10001)`
- Plot a 3D function, f, in the range x0 < x < x1 and y0 < y < y1, with a precision of prec and mode of either default, math, science, engineering, geoland, or geowater.<br>`Usage: Plot3D(f, x0, x1, y0, y1, mode='default', prec=101)`
- Plot a 2D quiver or vector plot of n by n vectors of a vector function f in the range x0 < x < x1 and y0 < y < y1. f should take in an x and y and return the vector components x and y at the point.<br>`Usage: PlotQuiver(f, x0, x1, y0, y1, n=21)`
- Plot a 3D quiver or vector plot of n by n by n vectors of a vector function f in the range x0 < x < x1, y0 < y < y1, and z0 < z < z1 with any of the same modes mentioned in plotting functions. f should take in an x, y, and z and return the vector components x, y, and z at the point.<br>`Usage: PlotQuiver3D(f, x0, x1, y0, y1, z0, z1, n=11, mode='')
- Plot a 2D scatter plot of data, a list of a tuple of an x coordinate, a y coordinate, and the point's name.<br>`Usage: PlotScatter(data)`
- Plot a 3D scatter plot of data, a list of a tuple of an x coordinate, a y coordinate, a z coordinate, and the point's name.<br>`Usage: PlotScatter3D(data)`
- Bar charts.<br>`Usage: PlotBar(data)`
- Pie Charts.<br>`Usage: PlotPie(data)`
- Table of values of `x` and `f(x)` given function f, range x0 < x < x1, stepsize step and rows r.<br>`Usage: PlotTable(f, x0, x1, step=1, r=4)`
- Plot n, a list of multiple numbers on a number line.<br>`Usage: PlotN(n)`
- Plot a finance plot containing net growth using data, a dict containing dates and corresponding values. <br>`Usage: PlotFinance(data: dict, title='Net Growth', relative=False)`
- Draw an angle of n radians inside a circle. <br>`Usage: PlotAngle(n: float)`

### Algebraic manipulation
- Add like terms.<br>`Usage: AddLike(terms)`
- Add unlike terms.<br>`Usage: Add(terms)`
- Multiply a list of terms.<br>`Usage: MultiplyTerms(terms)`
- Multiply out or expand a list of polynomials.<br>`Usage: MultiplyPoly(polynomials)`
- Exponentiate or expand a polynomial raised to a specific index.<br>`Usage: Exponentiate(polynomial, index)`

### Roots
- All roots of a smooth function f in a given range `-r < x < r`.<br>`Usage: Roots(f, r=100)`
- Sum and product of the roots of a polynomial<br>`Usage: SumOfRoots(polynomial)`<br>`ProductOfRoots(polynomial)`
- Degree of a polynomial.<br>`Usage: Degree(poly)`

### Differentiation
Valid operators include `+` `-` `*` `/` `^` and valid functions include `sin` `cos` `tan` `cot` `asin` `acos` `atan` `ln`.
Only `x` is a valid variable and symbolic constants such as `e` are not understood.
The differentiator can also correctly apply all of the following rules:
- Power rule
- Sum rule
- Difference rule
- Product rule
- Quotient rule
- Chain rule
```
Usage: 
D(f) for symbolic differentiation where f is the function to be differentiated.
Dn(f, x, prec=1e-15) for numeric differentiation where f is the function to be differentiated, x is the value at which gradient is to be found, and prec is the value of dx. Smaller the dx, the more accurate the result.
```
