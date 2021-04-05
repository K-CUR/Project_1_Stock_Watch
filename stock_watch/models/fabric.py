class Fabric:

    def __init__ (self, manufacturer, design_ref, main_colour, style, stock_price, sale_price, quantity, id = None):
        self.manufacturer = manufacturer
        self.design_ref = design_ref
        self.main_colour = main_colour
        self.style = style
        self.stock_price = stock_price
        self.sale_price = sale_price
        self.quantity = quantity
        self.id = id


    #METHODS

    def mark_up(self, stock_price, sale_price):
        mark_up = ((sale_price - stock_price)/stock_price)*100
        mark_up = round(mark_up,1)
        return str(mark_up)+"%"


    # def flag_low_stock(self, quantity):
    #     low_stock_threshold = 30
    #     if quantity < low_stock_threshold:
            # return "Low stock!"

    def flag_low_or_out_of_stock(self, quantity):
        low_stock_threshold = 30
        if quantity == 0 :
            return "Out of stock!"
        elif quantity < low_stock_threshold:
            return "Low stock!"
        else:
            return ""

