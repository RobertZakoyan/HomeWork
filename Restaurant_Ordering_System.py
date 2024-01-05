from abc import ABC, abstractmethod
from typing import List, Union, Optional, Any
class DishInfo(ABC):
    @abstractmethod
    def dish_info(self) -> str:
        pass

class MenuOperations(ABC):
    @abstractmethod
    def display_menu(self) -> str:
        pass

    @abstractmethod
    def change_price(self, dish_name: str, new_value: float) -> None:
        pass

class Dish(DishInfo):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.__price = price

    
        
    def dish_info(self) -> str:
        return f"{self.name} --> {self.__price}"
    

    @property
    def price(self) -> float:
        return self.__price
    

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise ValueError("The price can't be a negative")
        
class Appetizer(Dish):
    pass

class Entree(Dish):
    pass

class Desert(Dish):
    pass

class Menu(MenuOperations):
    def __init__(self, name: str, dishes: List['Dish']):
        self.name = name
        self.dishes = dishes

    def display_menu(self) -> str:
        menu_info = f"Menu for {self.name} \n"
        menu_info += "\n".join([dish.dish_info() for dish in self.dishes])
        return menu_info
    
    def change_price(self, dish_name: str, new_price: float) -> None:
        for dish in self.dishes:
            if dish.name == dish_name:
                dish.price = new_price
                return
        print("No such Dish in Menu")


    def get_dish_by_name(self, dish_name: str) -> Any:
        for dish in self.dishes:
            if dish.name == dish_name:
                return dish
        return "None"
    
    def __repr__(self):
        return self.name
class Order:
    def __init__(self, customer: 'Customer', dishes: List["Dish"]):
        self.customer = customer
        self.dishes = dishes
        self.total_price = sum([dish.price for dish in self.dishes])

    def display_order(self) -> str:
        orders = [dish.name for dish in self.dishes]
        return ", ".join(orders)
    
class Customer:
    def __init__(self, name: str, contact_info: str) -> None:
        self.name = name
        self.contact_info = contact_info
        self.order_history:List['Order'] = []

    def view_menu(self, menu: Menu) -> str:
        return menu.display_menu()
    
    def place_order(self, menu: Menu, dish_names: List[str]) -> Optional[Order]:

        dishes = [menu.get_dish_by_name(name) for name in dish_names if menu.get_dish_by_name(name) is not None]
        if not dishes:
            print("Invalid dish names. Please check the menu and try again.")
            return None
        
        order = Order(self, dishes)
        self.order_history.append(order)
        return order

    def view_order_history(self) -> str:
        history = [order.display_order() for order in self.order_history]
        return ", ".join(history)
    
    def get_bill(self) -> float:
        bill = 0.0
        for order in self.order_history:
            bill += order.total_price
        return bill

appetizer1 = Appetizer("Garlic Bread", 5.99)
appetizer2 = Appetizer("Bruschetta", 7.99)

entree1 = Entree("Spaghetti Bolognese", 12.99)
entree2 = Entree("Chicken Alfredo", 15.99)


desert1 = Desert("Lava Cake", 7.00)
desert2 = Desert("Brownie", 5.00)

menu = Menu("Italian Restaurant", [appetizer1, appetizer2, entree1, entree2, desert1, desert2])
menu.display_menu()

cusutomer = Customer("Robert", "mafrobo@gmail.com")

cusutomer.place_order(menu, ["Lava Cake", "Garlic Bread"])
cusutomer.place_order(menu,["Brownie", "Lava Cake"])

print(cusutomer.view_order_history())
print(cusutomer.get_bill())
print(cusutomer.view_menu(menu))