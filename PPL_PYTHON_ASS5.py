class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}, and I protect {self.city}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)  # Initialize parent class
        self.flight_speed = flight_speed

    def use_power(self):
        # Polymorphism: overridden method
        print(f"{self.name} soars through the sky at {self.flight_speed} km/h, using {self.power}!")


hero1 = Superhero("Shadow Strike", "Invisibility", "Metro City")
hero2 = FlyingHero("Skyblade", "Wind Slash", "Skyhaven", 800)

hero1.introduce()
hero1.use_power()
hero2.introduce()
hero2.use_power()        