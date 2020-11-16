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
- Return the list of factors of an integer, n.<br>`Usage: Factors(n: int)`
- Return a list of all the possible permutations of a list of items.<br>`Usage: Permutations(items: list)`
- Return the n<sup>th</sup> triangular number.<br>`Usage: Triangular(n: int)`
### Plotting
- 2D and 3D function plots
- 2D and 3D quiver plots or vector plots
- 2D and 3D scatter plots
- Bar charts
- Pie Charts
- Table of values of `x` and `f(x)` given function f
- Multiple numbers on Number line

### Roots
- All roots of a smooth function in a given range `-r < x < r`
- Sum and product of the roots of a polynomial
- Degree of a polynomial

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

![](C:\Users\melod\OneDrive\Pictures\ninja_logo.png)
