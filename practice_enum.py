# from enum import Enum

# class OrderStatus(Enum):
#     PLACED = "PLACED"
#     DELIVERY = "DELIVERY"
#     ACCEPTED = "ACCEPTED"

# status = OrderStatus.PLACED
# print(status)
# print(status.value)

# if status == OrderStatus.PLACED :
#     print("Order is placed")

# status = OrderStatus.ACCEPTED
# if status.value == "ACCEPTED":
#     print("Order is accepted")

# print(OrderStatus.PLACED.value)

from enum import Enum

class PaymentStatus(Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

print(PaymentStatus.FAILED)

status = PaymentStatus.SUCCESS
print(status.value)

if status.value == 'SUCCESS':
    print("Your Payment is Success, Thankyou")

print(PaymentStatus.SUCCES)