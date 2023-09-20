class Pilot1:
    def __init__(self,take_off,take_onn,fly,control_passengers,control_airplane):
        self.take_off = take_off
        self.take_onn = take_onn
        self.fly = fly
        self.control_passengers = control_passengers
        self.control_airplane = control_airplane

class MainPilot:
    def __init__(self,take_off,take_onn,control_passengers,control_airplane):
        super().__init__(take_off,take_onn,control_passengers,control_airplane)

    def change_direction(self,change_direction,control_extreme_take_onn):
        self.change_direction = change_direction
        self.extreme_take_off = control_extreme_take_onn

