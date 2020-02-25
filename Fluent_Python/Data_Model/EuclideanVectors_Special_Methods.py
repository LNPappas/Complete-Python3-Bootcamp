# Emulating Numeric Types Special Methods
# Euclidean Vectors: two-dimensional vectors
from math import hypot

class Vector:
    '''
        Euclidean Vector class
        Special Methods: __repr__, __abs__, __add__, __mul__
    '''

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # string representation of an object for inspection
    def __repr__(self):
        # %r = representation of object, now formatted to string
        # str '%s'.%(string) is formating similar to '{0}'.format(string)
        return 'Vector(%r, %r)' % (self.x, self.y)
        # or return 'Vector({0}, {1})'.format(self.x, self.y)

        # __str__ would return a string suitible for display to end users
        # while __repr__ can also do that, it's intention is for debugging and logging
        # if no custom __str__ Python calls __repr__ as fallback
        # so if only implimenting one use __repr__

    def __abs__(self):
        return hypot(self.x, self.y)

    # boolean statement returns False if magnitude of the vector is zero, else True
    def __bool__(self):
        return bool(abs(self))

    # adds two vectors creating new instance with result
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    # multiplies two vectors creating new instance with result
    def __mul__(self, scaler):
        return Vector(self.x*scaler, self.y*scaler)

if __name__ == "__main__":
    v1 = Vector(2,4)
    v2 = Vector(2,1)
    v3 = v1 + v2

    print("Vector(2, 4) + Vector(2, 1) =")
    print(v3)

    print('\nAbsolute Value of Vector(3, 4):')
    print(abs(Vector(3,4)))

    v = Vector(3,4)*3
    print("\nVector(3, 4)*3 = ",v)
    print('Absolute Value =', abs(v))

