import json

order = {
  "order_id": 1234,
  "status": "PLACED",
  "total": 540.00,
  "is_paid": True,
  "items": [
    {"name": "Chicken Biryani", "quantity": 2},
    {"name": "Raita", "quantity": 1}
  ]
}


print(type(order))
text = json.dumps(order)
print(type(text))

back = json.loads(text)
print(back["items"])
print(type(back))