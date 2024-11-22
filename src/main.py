from typing import List

class ShoppingCart:
    MAX_ITEMS = 100  # Maximum number of items allowed in the cart
    MAX_ITEM_NAME_LENGTH = 50  # Maximum length of item name
    ALLOWED_CHARACTERS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")

    def _init_(self) -> None:
        self._items: List[str] = []

    def add_item(self, item: str) -> None:
        if item is None:
            print("El item no puede ser None")
            return
        if item == "":
            print("El item no puede ser una cadena vacía")
            return
        if len(item) > self.MAX_ITEM_NAME_LENGTH:
            print(f"El item no puede superar los {self.MAX_ITEM_NAME_LENGTH} caracteres.")
            return
        if not all(char in self.ALLOWED_CHARACTERS for char in item):
            print("Item contiene caracteres no permitidos")
            return
        if len(self._items) >= self.MAX_ITEMS:
            print(f"El carrito está lleno. Máximo {self.MAX_ITEMS} items permitidos.")
            return 
        if item in self._items:
            print("El item ya existe en la lista")
        return
        self._items.append(item)

    def remove_item(self, item: str) -> None:
        if not isinstance(item, str):
            print("Item debe de ser una cadena de caracteres")
            return
        if item not in self._items:
            print(f"Item '{item}' no se encuentra en el carrito")
            return
        self._items.remove(item)

    def size(self) -> int:
        return print(len(self._items))

    def get_items(self) -> List[str]:
        return print(self._items)

    def clear(self) -> None:
        self._items.clear()

cart= ShoppingCart()
cart.add_item("book")
cart.add_item("book2")
cart.add_item("Esteesunstringdeexactamentecincuentacaracteressinsq")
cart.add_item(None)
cart.add_item("")
cart.add_item("book")
cart.get_items()
cart.add_item("book3")
cart.get_items()
cart.size()
cart.remove_item("book")
cart.get_items()
cart.size()
