def derive(f, x, h=0.0001):
    # Calculating the derivative using the definition: (f(x + h) - f(x - h)) / (2 * h)
    derivative = (f(x + h) - f(x - h)) / (2 * h)
    return derivative