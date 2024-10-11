class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.available_spots = total_spots

    def car_enter(self):
        if self.available_spots > 0:
            self.available_spots -= 1
            print(f"Car entered. Available spots: {self.available_spots}/{self.total_spots}")
        else:
            print("Parking lot is full.")

    def car_exit(self):
        if self.available_spots < self.total_spots:
            self.available_spots += 1
            print(f"Car exited. Available spots: {self.available_spots}/{self.total_spots}")
        else:
            print("Parking lot is empty.")

    def get_available_spots(self):
        return self.available_spots

# Create a parking lot with 10 spots
parking_lot = ParkingLot(10)

# Simulate cars entering and exiting
parking_lot.car_enter()  # Car enters
parking_lot.car_enter()  # Another car enters
parking_lot.car_exit()   # Car exits
parking_lot.car_enter()  # Car enters again
