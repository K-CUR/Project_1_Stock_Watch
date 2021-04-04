class Manufacturer:
    
    def __init__(self, name, sales_contact, active = True, id = None):
        self.name = name
        self.sales_contact = sales_contact
        self.active = active
        self.id = id

    
    def get_status(self):
        if self.active == True:
            return "Active"
        else:
            return "Deactivated"

    # MAY NEED
    # def mark_active(self):
    #     self.active = True
