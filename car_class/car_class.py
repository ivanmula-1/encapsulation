class Car:
def __init__(self, year_model, make):
        """Initialize the car's attributes."""
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
   
    def accelerate(self):
        """Add 5 to the current speed."""
        self.__speed += 5

    def brake(self):
        """Subtract 5 from the current 
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

     def get_speed(self):
        """Return the current speed."""
        return self.__speed

def main_car():
    my_car = Car("2024", "Toyota")

    print ("\n--- ACCELERATING ---")
    for i in range(5):
        my_car.accelerate()
        print(f"Current speed after acceleration {i + 1}: {my_car.get_speed()}") 

    print("\n--- BRAKING ---")
    for i in range(5):
        my_car.brake()
        print(f"Current speed after brake {i + 1}: {my_car.get_speed()}")


if __name__ == "__main__":
    main_car()
