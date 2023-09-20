class MyClass:

    def __init__(self,model,color,year):
        self.model = model
        self.color = color
        self.year = year
    def stop(self):
        print('Mashina ostanovis')
    def change_color(self,new_color):
        self.color= new_color

gentra = MyClass('Chevrolet', 'Black',2022)

gentra.change_color('White')
print(gentra.color)
