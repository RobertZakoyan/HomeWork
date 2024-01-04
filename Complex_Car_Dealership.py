from abc import ABC, abstractmethod
from typing import Union, List, Dict

class Car(ABC):
    @abstractmethod
    def __init__(self, make:str, model: str, price: float, tank_capacity:int, battery_capacity:int) ->None:
        self._make = make
        self._model = model
        self._price = price
        self._tank_capacity = tank_capacity
        self._battery_capacity = battery_capacity
    @abstractmethod
    def display_info(self) -> str:
        pass

class SalesOperations(ABC):
    @abstractmethod
    def make_sale(self, customer: "Customers", car: "Car") -> None:
        pass
        


class EngineCar(Car):
    def __init__(self, make: str, model: str, price: float, tank_capacity: int) -> None:
        self._make = make
        self._model = model
        self._price = price
        self._tank_capacity = tank_capacity

    def display_info(self) -> str:
        return f"{self._make}\{self._model},  Price --> {self._price},  Tank Capacity --> {self._tank_capacity}L"

        
class ElectricCar(Car):
    def __init__(self, make: str, model: str, price: float, battery_capacity: int) -> None:
        self._make = make
        self._model = model
        self._price = price
        self._battery_capacity = battery_capacity

    def display_info(self) -> str:
        return f"{self._make}\{self._model},  Price --> {self._price},  Battery Capacity --> {self._battery_capacity}mAH"
    
class HybridCar(Car):
    def __init__(self, make: str, model: str, price: float, battery_capacity: int, tank_capacity:int) -> None:
        self._make = make
        self._model = model
        self._price = price
        self._battery_capacity = battery_capacity
        self._tank_capacity = tank_capacity
    def display_info(self) -> str:
        return f"{self._make}\{self._model},  Price --> {self._price}, Tank Capacity --> {self._tank_capacity}L,  Battery Capacity --> {self._battery_capacity}mAH"
class Customers:
    def __init__(self, name: str, contact_info: str) -> None:
        self._name = name
        self._contact_info = contact_info

class SalesPeople:
    def __init__(self, name: str, commision_rate: float) -> None:
        self._name = name
        self._commision_rate = commision_rate
        self._sales_history: List[Dict[str, 'Union[str, float, object]']] = []

    def make_sale(self, customer:"Customers", car:"Car"):
        profit = car._price * self._commision_rate
        update_info = {
            "Customer" : customer._name,
            "Car": f"{car._make}\{car._model}",
            "Commision for sale": profit
        }
        self._sales_history.append(update_info)

    def show_history(self):
        print(self._sales_history)

car_1 = HybridCar("Toyota", "Rav-4", 24000, 3000, 70)
car_2 = EngineCar("Mazda", "Cx-3", 21000, 80)

print(car_1.display_info())

customer_1 = Customers("Rob", "+37498700822")

sales_people = SalesPeople("Hakob", 0.01)

sales_people.make_sale(customer_1, car_1)
sales_people.show_history()
    


