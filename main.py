class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")


class Truck(Vehicle):
    def __init__(self, make, model, year, bed_size):
        super().__init__(make, model, year)
        self.bed_size = bed_size

    def display_info(self):
        super().display_info()
        print(f"Bed size: {self.bed_size}")


def create_car():
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    year = input("Enter the year of the car: ")
    num_doors = input("Enter the number of doors of the car: ")
    
  


def create_truck():
    make = input("Enter the make of the truck: ")
    model = input("Enter the model of the truck: ")
    year = input("Enter the year of the truck: ")
    bed_size = input("Enter the bed size of the truck: ")
    return Truck(make, model, year, bed_size)


def main():
    while True:
        print( )
        print("--- Welcome to Frias Virtual Garage ---")
        print("1. Create a car")
        print("2. Create a truck")
        print("3. Exit")
        print()
        choice = input("Enter your choice (1-3): ")
        print()

        if choice == "1":
            car = create_car()
            print()
            print("Car Created:")
            car.display_info()
            
        elif choice == "2":
            truck = create_truck()
            print()
            print("Truck Created:")
            truck.display_info()
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
  

    main()
