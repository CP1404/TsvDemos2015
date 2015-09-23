__author__ = 'sci-lmw1'
# Car class example
# the client code is down the bottom for convenience, but would usually be in a separate file


class Car:
    def __init__(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel
        or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance


class Taxi(Car):
    def __init__(self, name, fuel, price_per_km):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, ${:.2f}/km, {}km on current fare".format(super().__str__(), self.price_per_km, self.current_fare_distance)

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel, 1.2)
        self.fanciness = fanciness

    def get_fare(self):
        return SilverServiceTaxi.flagfall + (super().get_fare() * self.fanciness)


def test():
    # bus = Car("Datsun", 180)
    # bus.drive(30)
    # print("fuel =", bus.fuel)
    # print("odo =", bus._odometer)
    # bus.drive(55)
    # print("fuel =", bus.fuel)
    # print("odo = ", bus._odometer)
    # print(bus)
    #
    # # drive bus (input/loop is oblivious to fuel)
    # distance = int(input("Drive how far? "))
    # while distance > 0:
    #     travelled = bus.drive(distance)
    #     print(bus)
    #     distance = int(input("Drive how far? "))

    t = Taxi("Prius 1", 100, 1.2)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())

    sst = SilverServiceTaxi("Limo", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())

if __name__ == "__main__":
    test()
