class Cake:
    def __init__(self, full_name , qty_on_hand, manufacture_cost, selling_price, baker, category, vegetarian, daily_sales_forecast, par_level, id = None):
            self.full_name = full_name 
            self.qty_on_hand = qty_on_hand 
            self.manufacture_cost = manufacture_cost
            self.selling_price = selling_price
            self.baker = baker
            self.category = category
            self.vegetarian = vegetarian
            self.daily_sales_forecast = daily_sales_forecast
            self.par_level = par_level
            self.id = id

    def profit_margin(self):
        margin = self.selling_price - self.manufacture_cost
        return margin

    def is_stock_low(self):
        return self.qty_on_hand < self.par_level

    
         



    def out_of_stock():
        pass
