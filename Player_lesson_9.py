class Player:
    def __init__(self,stamina,power,accuracy,speed):
        self.stamina = stamina
        self.power = power
        self.accuracy = accuracy
        self.speed = speed

class Attacker:
    def __init__(self,stamina,power,accuracy,speed):
        super().__init__(stamina,power,accuracy,speed)

    def goal(self,goal):
        self.goal = goal

class Goalkeeper:
    def __init__(self,stamina,power,accuracy):
        super().__init__(stamina,power,accuracy)

    def catch_boll(self,catch_boll):
        self.catch_boll = catch_boll

class Zashitnik:
    def __init__(self,power,accuracy,speed):
        super().__init__(power,accuracy,speed)

    def protect(self,protect):
        self.protect = protect

class Poluzashitnik:
    def __init__(self,stamina,power,accurasy,speed):
        super().__init__(stamina,power,accurasy,speed)

    def pas(self,pas):
        self.pas = pas

