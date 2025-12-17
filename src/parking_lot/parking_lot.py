from enum import Enum
from typing import Optional

"""
Design a parking lot

use cases:
1. park a vehicle
2. remove a vehicle
3. count free spots
4. find where a vehicle is parked
5. know if the lot is full

core entities:
1. parking lot
    - a list of parking spots
    - is_full: boolean

2. parking spot
    - spot_id
    - has_vehicle: boolean
3. vehicle
    - license plate
    - vehicle type
"""


class VehicleType(Enum):
    SEDAN = "sedan"
    SUV = "suv"
    TRUCK = "truck"
    MOTORCYCLE = "motorcycle"


class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def __repr__(self):
        """returns a string representation of the object"""
        return f"Vehicle({self.license_plat}, {self.vehicle_type})"


class ParkingSpot:
    def __init__(self, spot_id: int):
        self.spot_id = spot_id
        self.vehicle = None

    @property
    def is_free(self):
        return self.vehicle is None

    def park(self, vehicle: Vehicle) -> bool:
        if not self.is_free:
            return False
        self.vehicle = vehicle
        return True

    def remove_vehicle(self) -> Optional[Vehicle]:
        v = self.vehicle
        self.vehicle = None
        return v


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.spots = [ParkingSpot(i) for i in range(self.capacity)]
        self.available_spots = capacity
        self.vehicle_map: dict[str, ParkingSpot] = {}

    @property
    def is_full(self):
        return self.available_spots == 0

    def park_vehicle(self, vehicle: Vehicle) -> Optional[int]:
        """Park vehicle in first available spot, return sport_id or None"""
        if self.is_full:
            return None

        if vehicle.license_plate in self.vehicle_map:
            return self.vehicle_map[vehicle.license_plate]

        for spot in self.spots:
            if spot.is_free:
                spot.park(vehicle)
                self.available_spot -= 1
                return spot.spot_id

    def remove_vehicle(self, license_plate: str) -> bool:
        spot = self.vehicle_map.get(license_plate)
        if spot is None:
            return False

        spot.remove_vehicle()
        del self.vehicle_map[license_plate]
        self.available_spot += 1
        return True

    def __repr__(self):
        pass
