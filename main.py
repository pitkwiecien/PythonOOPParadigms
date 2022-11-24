from abstraction import square
from abstraction import triangle

square = square.Square()
triangle = triangle.Triangle()

print(square.get_sides())
print(triangle.get_sides())

print(square.return_hello())
print(triangle.return_hello())