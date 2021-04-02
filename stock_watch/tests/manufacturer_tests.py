import unittest
from models.manufacturer import Manufacturer


class TestManufacturer (unittest.TestCase):

    def setUp(self):
        self.manufacturer = Manufacturer("Harlequin Ltd", "John Barrows", True)


        
    def test_manufacturer_has_name(self):
        self.assertEqual("Harlequin Ltd", self.manufacturer.name)
        
    def test_manufacturer_has_sale_contact(self):
        self.assertEqual("John Barrows", self.manufacturer.sales_contact)

    def test_manufacturer_is_active(self):
        self.assertEqual(True, self.manufacturer.active)


