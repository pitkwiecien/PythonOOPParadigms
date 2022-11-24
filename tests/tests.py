from unittest import TestCase

from classes.square import Square
from classes.triangle import Triangle
from classes.polygon import Polygon
import auxiliary_functions


class AbstractionTests(TestCase):
    def __init__(self, *args, **kwargs):
        super(AbstractionTests, self).__init__(*args, **kwargs)
        error_occurred = False
        try:
            self.sq = Square()
            self.tr = Triangle()
        except TypeError:
            error_occurred = True

        self.assertFalse(error_occurred)

    def test_abstract_implemented(self):
        self.assertEqual(self.sq.get_sides(), 4)
        self.assertEqual(self.tr.get_sides(), 3)

    def test_abstract_not_implemented(self):
        class Temporary(Polygon):
            pass

        error_occurred = False
        try:
            _ = Temporary()
        except TypeError:
            error_occurred = True

        self.assertTrue(error_occurred)

    def test_class_method(self):
        self.assertEqual(self.sq.return_hello(), "hello")
        self.assertEqual(self.tr.return_hello(), "triangle")

    def test_abstract_instantiation(self):
        error_occurred = False
        try:
            _ = Polygon()
        except TypeError:
            error_occurred = True

        self.assertTrue(error_occurred)

    def test_polymorphism(self):
        error_occurred = False
        eq = None
        try:
            eq = auxiliary_functions.call_get_sides(self.sq)
        except RuntimeError:
            error_occurred = True

        self.assertFalse(error_occurred)
        self.assertEqual(eq, self.sq.get_sides())
