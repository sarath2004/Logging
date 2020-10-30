import inspect
import logging

logging.basicConfig(filename="Parameters Specified.log", level=logging.INFO)


class Car:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(Car, key, value)

    def getKeys(self):
        keys = []
        for i in inspect.getmembers(car1):
            if i[0].startswith("_") is False:
                if inspect.ismethod(i[1]) is False:
                    key, _ = i
                    keys.append(key)
        return keys

    def getValues(self):
        values = []
        for i in inspect.getmembers(car1):
            if i[0].startswith("_") is False:
                if inspect.ismethod(i[1]) is False:
                    _, value = i
                    values.append(value)
        return values

    def carInfo(self):
        logging.info(
            "The Parameters Specified For Your {} Are {} And {}".format(
                car1.getValues()[0], car1.getKeys()[2], car1.getKeys()[1]
            )
        )


car1 = Car(speed=60, condition="Good", company="Nissan Altima")
car1.carInfo()
