# it is about implementing some kind of hierarchy

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        # code to start the vehicle
        pass

    def stop(self):
        # code to stop the vehicle
        pass


class Car(Vehicle):
    def __init__(self, make, model, doors_qty):
        super().__init__(make, model)
        self.doors_qty = doors_qty

    def lock_doors(self):
        # code to lock doors
        pass

    def open_doors(self):
        # code to open doors
        pass


class Motorbike(Vehicle):
    def __init__(self, make, model, wheels_qty):
        super().__init__(make, model)
        self.wheels_qty = wheels_qty

    def something(self):
        # code for it
        pass
