from abstraction.polygon import Polygon


class Triangle(Polygon):
    def get_sides(self):
        return 3

    def return_hello(self):
        return "triangle"
