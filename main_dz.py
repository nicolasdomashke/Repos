from math import sqrt

a, b, c = map(int, input().split())

d = b * b - 4 * a * c
if d < 0:
    print("no solutions")
elif d == 0:
    x = -b / (2 * a)
    print("found one solution:")
    print(x)
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("found two solutions:")
    print(x1, x2)
