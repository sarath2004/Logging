import logging

logging.basicConfig(filename="Car Info.log", level=logging.INFO)


class Car:
    def __init__(self, speed, condition):
        self.speed = speed
        self.condition = condition

    def carInfo(self):
        logging.info(
            "Your current speed is {}km / hr and the condition of your car is {}".format(
                self.speed, self.condition
            )
        )

    def argsReturn(self):
        for key in car1.__dict__.keys():
            print(key)


car1 = Car(speed=60, condition="Good")
car1.carInfo()
car1.argsReturn()
