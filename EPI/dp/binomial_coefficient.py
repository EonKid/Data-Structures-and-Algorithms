"""
The symbol (") is the short form for the expression ■ If is the number of ways to choose a fc-element subset from an n-element set.
 It is not obvious that the expression defining (") always yields an integer.
  Furthermore, direct computation of (") from this expression quickly results in the numerator or denominator overflowing
   if integer types are used, even if the final result fits in a 32-bit integer.
    If floats are used, the expression may not yield a 32-bit integer.
Design an efficient algorithm for computing (") which has theproperty that it never overflows
 if the final result fits in the integer word size.

"""

T = {}


def binomial_coefficient(n: int, k: int):
    if (n, k) not in T:
        if k == 0 or n == k:
            return 1
        T[n, k] = binomial_coefficient(n-1, k) + binomial_coefficient(n - 1, k - 1)
    return T[n,k]


print("binomial coefficient: ", binomial_coefficient(5, 2))

