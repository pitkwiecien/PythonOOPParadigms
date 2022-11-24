from classes import square, triangle

square = square.Square()
triangle = triangle.Triangle()

print(square.get_sides())
print(triangle.get_sides())

print(square.return_hello())
print(triangle.return_hello())

print(square.dimensions)
square.dimensions = "3D"
print(square.dimensions)