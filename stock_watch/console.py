import pdb

from models.manufacturer import Manufacturer
from models.fabric import Fabric

import repositories.manufacturer_repository as manufacturer_repository
import repositories.fabric_repository as fabric_repository


fabric_repository.delete_all()
manufacturer_repository.delete_all()

# MANUFACTURERS
manufacturer_1 = Manufacturer("Harlequin Ltd", "John Barrows", True)
manufacturer_repository.save(manufacturer_1)

manufacturer_2 = Manufacturer("Villa Nova Ltd", "Sandra Davies", True)
manufacturer_repository.save(manufacturer_2)

manufacturer_3 = Manufacturer("Denholm & Sons", "Kelly Dunbar", False)
manufacturer_repository.save(manufacturer_3)

# FABRICS
fabric_1 = Fabric(manufacturer_1, "Nena01", "Green", "Plain", 12.00, 18.00, 26)
fabric_repository.save(fabric_1)

fabric_2 = Fabric(manufacturer_1, "Nena02", "Blue", "Plain", 12.00, 18.00, 32)
fabric_repository.save(fabric_2)

fabric_3 = Fabric(manufacturer_1, "Nena03", "Grey", "Plain", 12.00, 18.00, 40)
fabric_repository.save(fabric_3)

fabric_4 = Fabric(manufacturer_2, "Satori08", "White", "Stripe", 16.00, 20.00, 22)
fabric_repository.save(fabric_4)

fabric_5 = Fabric(manufacturer_2, "Satori21", "Red", "Stripe", 16.00, 20.00, 33)
fabric_repository.save(fabric_5)

fabric_6 = Fabric(manufacturer_2, "Bella25", "Pink", "Floral", 18.00, 27.00, 50)
fabric_repository.save(fabric_6)

fabric_7 = Fabric(manufacturer_3, "Easter Bunny", "White", "Illustration", 8.00, 13.00, 12)
fabric_repository.save(fabric_7)



pdb.set_trace()