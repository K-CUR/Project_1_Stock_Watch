import unittest
from models.fabric import Fabric


class TestFabric (unittest.TestCase):

    def setUp(self):
        self.fabric = Fabric("Harlequin", "Nena01", "Green", "Plain", 12.00, 18.00, 26)
        self.fabric_2 = Fabric("Harlequin", "Nena02", "Blue", "Plain", 12.00, 18.00, 0)
        self.fabric_3 = Fabric("Harlequin", "Nena03", "Red", "Plain", 12.00, 18.00, 40)
   
    def test_fabric_has_manufacturer(self):
        self.assertEqual("Harlequin", self.fabric.manufacturer)
    
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
        actual = self.fabric.flag_low_or_out_of_stock(self.fabric.quantity)
        self.assertEqual("Low stock!", actual)

    def test_fabric_flags_out_of_stock(self):
        actual = self.fabric.flag_low_or_out_of_stock(self.fabric_2.quantity)
        self.assertEqual("Out of stock!", actual)

    def test_fabric_flags_in_stock(self):
        actual = self.fabric.flag_low_or_out_of_stock(self.fabric_3.quantity)
        self.assertEqual("", actual)
