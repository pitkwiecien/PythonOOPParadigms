import abc


class Polygon(abc.ABC):
    @abc.abstractmethod
    def get_sides(self):
        pass

    def return_hello(self):
        return "hello"
