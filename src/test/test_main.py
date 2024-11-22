import pytest
from src.main import ShoppingCart
from typing import List

@pytest.fixture
def empty_cart():
    return ShoppingCart()

@pytest.mark.parametrize("items", [
    ([]),
    (["apple"]),
    (["apple", "banana"]),
    (["apple", "banana", "orange"]),
    (["12345"])
])
def test_add_item_and_size(empty_cart: ShoppingCart, items: List[str]):
    for item in items:
        empty_cart.add_item(item)
    
    assert empty_cart.size() == len(items)
    assert empty_cart.get_items() == items

@pytest.mark.parametrize("items, expected_size", [
    ([], 0),
    (["apple"], 1),
    (["apple", "banana"], 2),
    (["apple", "banana", "orange"], 3),
    (["12345"], 1)
])
def test_size(empty_cart: ShoppingCart, items: List[str], expected_size: int):
    for item in items:
        empty_cart.add_item(item)
    
    assert empty_cart.size() == expected_size

@pytest.mark.parametrize("items", [
    ([]),
    (["apple"]),
    (["apple", "banana"]),
    (["apple", "banana", "orange"]),
    (["12345"])
])
def test_get_items(empty_cart: ShoppingCart, items: List[str]):
    for item in items:
        empty_cart.add_item(item)
    
    assert empty_cart.get_items() == items

@pytest.mark.parametrize("initial_items, item_to_add, expected_items", [
    ([], "apple", ["apple"]),
    (["banana"], "apple", ["banana", "apple"]),
    (["banana", "orange"], "apple", ["banana", "orange", "apple"])
])
def test_add_item(empty_cart: ShoppingCart, initial_items: List[str], item_to_add: str, expected_items: List[str]):
    for item in initial_items:
        empty_cart.add_item(item)
    
    empty_cart.add_item(item_to_add)
    assert empty_cart.get_items() == expected_items
