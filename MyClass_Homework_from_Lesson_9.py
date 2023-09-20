class House:
    def __init__(self,region,location,price,style):
        self.region = region
        self.location = location
        self.price = price
        self.style = style

    def change_region(self,new_region):
        self.region = new_region

    def change_location(self,new_location):
        self.location = new_location

    def change_price(self,new_price):
        self.price = new_price

    def change_style(self,new_style):
        self.style = new_style

    def stop(self):
        print('House was founded')

home = House('Philodelphi','Fylend',200000,'modern')

home.change_price(350000)
print(home.change_price)