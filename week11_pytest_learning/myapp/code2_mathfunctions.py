class Algebra:
    @staticmethod
    def square(x):
        return x ** 2

    @staticmethod
    def cube(x):
        return x ** 3


class Geometry:
    @staticmethod
    def is_triangle(a, b, c):
        return a + b + c == 180

    @staticmethod
    def is_quadrilateral(w, x, y, z):
        return w + x + y + z == 360
