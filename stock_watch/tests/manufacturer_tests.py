import unittest
from models.manufacturer import Manufacturer


class TestManufacturer (unittest.TestCase):

    def setUp(self):
        self.manufacturer = Manufacturer("Harlequin Ltd", "John Barrows", True)


        
    def test_manufacturer_has_name(self):
        self.assertEqual("Harlequin Ltd", self.manufacturer.name)
        
    def test_manufacturer_has_sale_contact(self):
        self.assertEqual("John Barrows", self.manufacturer.sales_contact)

    # def test_manufacturer_is_active(self):
    #     actual = self.manufacturer.status()
    #     self.assertEqual("Active", actual)


    def test_status(self):
        self.assertEqual("Active", self.manufacturer.get_status())

    


