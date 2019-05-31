def product(fraction):
    product = reduce(lambda x,y: x * y, fraction)
    num = product.numerator
    den = product.denominator
    return num, den
