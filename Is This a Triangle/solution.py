# 7 kyu problem
# Implement a method that accepts 3 integer values a, b, c.
# The method should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

Solution:
def is_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    else:
        return False