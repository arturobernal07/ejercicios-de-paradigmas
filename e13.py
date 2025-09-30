class Vector4D:
    def __init__(self, u, v, x, y):
        self.u = u
        self.v = v
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector4D(self.u + otro.u, self.v + otro.v, self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Vector4D(self.u - otro.u, self.v - otro.v, self.x - otro.x, self.y - otro.y)

    def __mul__(self, otro):
        return Vector4D(self.u * otro.u, self.v * otro.v, self.x * otro.x, self.y * otro.y)

    def __truediv__(self, escalar):
        return Vector4D(self.u / escalar, self.v / escalar, self.x / escalar, self.y / escalar)

    def __str__(self):
        return f"({self.u}, {self.v}, {self.x}, {self.y})"


vector_1 = Vector4D(1,3,2,4)
vector_2 = Vector4D(9,8,6,7)

print("Vector 1 + Vector 2 =", vector_1 + vector_2)
print("Vector 1 * Vector 2 =", vector_1 * vector_2)
print("Vector 1 - Vector 2 =", vector_1 - vector_2)
print("Vector 2 / 2 =", vector_2 / 2)
