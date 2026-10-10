# class MenuItems:
#     def __init__(self,item_id,name,price):
#         self.item_id = item_id
#         self.name = name
#         self.price = price


# item = MenuItems(101,"Pulav",250)
# print(item)
# print(item.name)

# from dataclasses import dataclass
# @dataclass
# class MenuItems:
#     item_id:int
#     name : str
#     price : float


# item = MenuItems(1,"Rotti",80)
# print(item)
# print(item.name)

# from dataclasses import dataclass

# @dataclass
# class menuItems:
#     name:str
#     age:int
#     order_items:list[str]
#     is_open :bool =True

# ord = menuItems('RAM',22,['Pannier','Rotti'])
# print(ord)
# print(ord.order_items)
# ord.age  = 23
# print(ord.age)
# print(ord)

from dataclasses import dataclass

@dataclass(frozen=True)
class Address:
    city : str
    pincode : int

adr = Address('Jaipur',323323)
print(adr)
print(adr.city)
adr.city = 'hyd'



