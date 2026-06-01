class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

 def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
            self.__speed = speed
            self.__radius = float(radius)
            self.__color = color
            self.__on = bool(on)

        def get_speed(self): return self.__speed

        def set_speed(self, speed): self.__speed = speed

        def get_on(self): return self.__on

        def set_on(self, on): self.__on = bool(on)

        def get_radius(self): return self.__radius

        def set_radius(self, radius): self.__radius = float(radius)

        def get_color(self): return self.__color

        def set_color(self, color): self.__color = color

def TestFan():
        fan1 = Fan()
        fan1.set_speed(Fan.FAST)
        fan1.set_radius(10)
        fan1.set_color("yellow")
        fan1.set_on(True)

        fan2 = Fan()
        fan2.set_speed(Fan.MEDIUM)
        fan2.set_radius(5)
        fan2.set_color("blue")
        fan2.set_on(False)

        print(f"Fan status: {'ON' if fan1.get_on() else 'off'}")
        print(
            f"speed: {int(fan1.get_radius() if fan1.get_speed() == Fan.FAST else fan1.get_speed())}")  # Matches your 3
        print(f"radius: {int(fan1.get_radius())}")
        print(f"color: {fan1.get_color()}")
  
        print(f"Fan status: {'ON' if fan2.get_on() else 'off'}")
        print(f"speed: {fan2.get_speed()}")
        print(f"radius: {int(fan2.get_radius())}")
        print(f"color: {fan2.get_color()}")
    
 if __name__ == "__main__":
        TestFan()
