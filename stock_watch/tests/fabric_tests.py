import unittest
from models.fabric import Fabric


class TestFabric (unittest.TestCase):

    def setUp(self):
        self.fabric = Fabric("Nena01", "Green", "Plain", 12.00, 18.00, 26)

    
    
    def test_fabric_has_design_ref(self):
        self.assertEqual("Nena01", self.fabric.design_ref)

    def test_fabric_has_main_colour(self):
        self.assertEqual("Green", self.fabric.main_colour)

    def test_fabric_has_style(self):
        self.assertEqual("Plain", self.fabric.style)

    def test_fabric_has_stock_price(self):
        self.assertEqual(12.00, self.fabric.stock_price)

    def test_fabric_has_sale_price(self):
        self.assertEqual(18.00, self.fabric.sale_price)

    def test_fabric_has_sale_quantity(self):
        self.assertEqual(26, self.fabric.quantity)

    def test_fabric_mark_up(self):
        actual = self.fabric.mark_up(self.fabric.stock_price, self.fabric.sale_price)
        self.assertEqual("50.0%", actual)

    def test_fabric_flags_low_stock(self):
        actual = self.fabric.flag_low_stock(self.fabric.quantity)
        self.assertEqual("Low stock!", actual)
