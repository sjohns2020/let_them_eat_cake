class Inventory:

    def __init__(self, full_name, available_funds):
        self.full_name = full_name 
        self.available_funds = available_funds
        self.cakes = []
        self.bakers = []
    
    def sort_cakes(self):
        self.cakes.sort()

    def create_baker():
        pass
    def show_baker():
        pass
    def update_baker():
        pass
    def remove_baker():
        pass

    def create_cake():
        pass
    def show_cake():
        pass
    def update_cake():
        pass
    def remove_cake():
        pass

    def list_of_categories():
        pass

    def list_of_vegetarian_cakes():
        pass

    def list_of_low_stock_cakes(self):
        low_stock_cakes = []
        for cake in self.cakes:
            if cake.qty_on_hand < cake.par_level:
                low_stock_cakes.append(cake)
        return low_stock_cakes
        

    def list_of_out_of_stock_cakes():
        pass


    def most_profitable_cake():
        pass
    def most_productive_baker():
        pass

    def cost_of_goods():
        pass