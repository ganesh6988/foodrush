# def add(a,b):
#     print(a+b)

# def sum(a,b):
#     return a+b


# add(2,3)
# y = sum(2,3)

# print(y)

# def apply_discount(price,discount=10):
#     print(price - (price * discount/100))

# print(apply_discount(1000))
# print(apply_discount(1000,20)

# def total(*prices):
#     return sum(prices)

# print(total(100,200,300,300))

# def create_user(**detials):
#     return detials

# print(create_user(name = "abc",age = 22, order = "placed"))


# def calculate_total(price:float, quantity:int)-> float:
#     return price * quantity

# print(type(calculate_total(10,2)))


# def add_item(item, cart=[]):
#     cart.append(item)
#     return cart

# print(add_item("shoes"))
# print(add_item("shocks"))

# def add_item(item, cart=None):
#     if cart is None:
#         cart = []
#     cart.append(item)
#     return cart

# print(add_item("Shoes"))
# print(add_item("snna"))

# def items(*items):
#     return items*2

# x = items(1,2,3,4)
# print(x)


# def safe_division(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print(f"cannot divide by zero")
#     else:
#         print(f"{result} is successful")
#     finally:
#         print("safe division is successfull")

# safe_division(10,2)


# def place_order(stock,quantity):
#     if quantity > stock:
#         return 





# with open("notes.txt","w", encoding="utf-8") as f:
#     f.write("Hello\n")
#     f.write("Guru\n")

# with open("notes.txt","r",encoding="utf-8") as f:
#     content = f.read()

# print(content)

# with open("notes.txt","a",encoding="utf-8") as f:
#     f.write("Bye")

# with open("notes.txt","r",encoding="utf-8") as f:
#     content = f.read()

# print(content)

# with open("notes.txt","w", encoding="utf-8") as f:
#     f.write("Bye")

# with open("notes.txt","r",encoding="utf-8") as f:
#     content = f.read()

# print(content)

# with open("notes.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())


# with open("app.log","w",encoding ="utf-8") as f:
#     f.write("server stated\n")

# def read_config(path):
#     try:
#         with open(path,"r",encoding="utf-8") as f:
#             return f.read()
#     except FileNotFoundError:
#         print(f"Config file not found:{path}")
#         return None
#     except PermissionError:
#         print(f"No permission to read: {path}")
#         return None

# f = read_config("app.log")
# print(f)


# import json
# user = {"name": "Luc", "age": 21, "is_active": True,"address":None}

# json_text = json.dumps(user)
# print(json_text)
# print(type(json_text))

# data = json.loads(json_text)
# print(data)

# order ={
#     "order_id":101,
#     "item":[
#         {"product_id":5, "qty":2,"price":1299},
#         {"product_id":4, "qty":4, "price":14999},
#     ]
# }

# total = 0

# total = sum(items['qty'] * items['price'] for items in order['item'])
# print(total)


    
import json
from pathlib import Path


class OutOfStockError(Exception):
    """Stock takkuva unte raise chestam."""


def load_products(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Products file not found: {path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Products file has invalid JSON: {e}")


def calculate_total(price: int, qty: int) -> int:
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0")
    return price * qty


def place_order(products: dict, product_id: str, qty: int) -> dict:
    product = products.get(product_id)
    if product is None:
        raise KeyError(f"Product {product_id} not found")
    if qty > product["stock"]:
        raise OutOfStockError(f"Only {product['stock']} left")
    return {
        "product": product["name"],
        "qty": qty,
        "total": calculate_total(product["price"], qty),
    }


if __name__ == "__main__":
    # sample products file create chestunnam
    sample = {
        "p1": {"name": "Shoes", "price": 999, "stock": 5},
        "p2": {"name": "Shirt", "price": 499, "stock": 0},
    }
    Path("products.json").write_text(json.dumps(sample, indent=2), encoding="utf-8")

    products = load_products("products.json")

    for pid, qty in [("p1", 2), ("p2", 1), ("p9", 1), ("p1", -3)]:
        try:
            print("OK:", place_order(products, pid, qty))
        except OutOfStockError as e:
            print("Out of stock:", e)
        except KeyError as e:
            print("Not found:", e)
        except ValueError as e:
            print("Invalid input:", e)