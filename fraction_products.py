from math import gcd
from functools import reduce

#doing the multiplication of numerators and denominators
def product_fraction(tup):
    product = reduce(lambda x,y: x * y, tup)
    return product

#a function to return greatest common divisor
def finding_gcd(x, y):
    divisor = gcd(x, y)
    return divisor

#dividing the fraction's numerator and denominator and turn them into integers
def dividing(number, div):
    final = number / div
    return int(final)

#start input to receive the number of fractions
n = int(input())
fractions = []
numerators = []
denominators = []
if n >= 1 and n <= 100:
    #adding fractions in the tuple
    for i in range(n):
        fractions.append(input())
        frct = fractions[i]
        num, den = frct.split(' ')
        numerators.append(int(num))
        denominators.append(int(den))

    #using the functions
    num_prod = product_fraction(numerators)
    den_prod = product_fraction(denominators)

    div = finding_gcd(num_prod, den_prod)

    num_final = dividing(num_prod, div)
    den_final = dividing(den_prod, div)

    #putting the results in the same variable and outputting it
    product = str(num_final) + ' ' + str(den_final)
    print(product)

#HackerRank
"""
from fractions import Fraction
from functools import reduce

#I made this function just to pass in the HackerRank
def product(fraction):
    product = reduce(lambda x,y: x * y, fraction)
    num = product.numerator
    den = product.denominator
    return num, den
#finished my func

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
"""
#looking for what I did here, my script is much more extensive than HackerRank's code
