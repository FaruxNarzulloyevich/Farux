class Worker:
    def __init__(self,name,position):
        self.name = name
        self.position = position

class HR(Worker):
    def __init__(self,name,position):
        super().__init__(name,position)

    def show_position(self,name):
        return name.position

jordan = Worker('Jordan','Junior')
pavel = HR('Pavel','HR')
print(pavel.show_position(jordan))