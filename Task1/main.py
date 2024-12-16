from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, region_spec: str):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.region_spec}): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.region_spec}): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


# Приклад використання
def main() -> None:
    # Створення фабрик для різних регіонів
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    # Створення транспортних засобів для США
    us_car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    us_car.start_engine()
    us_motorcycle.start_engine()

    # Створення транспортних засобів для ЄС
    eu_car = eu_factory.create_car("Volkswagen", "Golf")
    eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1200")

    eu_car.start_engine()
    eu_motorcycle.start_engine()


if __name__ == "__main__":
    main()
