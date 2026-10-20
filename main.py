
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/restaurants")
# def get_restaurants():
#     return ["Spice Garden", "Pizza Point"] 

# @app.get("/")
# def home():
#     return {"message":"Welcome to FoodRush"}

# @app.get("/about")
# def about():
#     return {"app":"FoodRush","Version":1} 


from fastapi import FastAPI, HTTPException

app = FastAPI()

restaruants = {
    1: {"id":1, "name":"Spicy Garden","cusine":"indian"},
    2: {"id":2, "name":"Pizza Point","cusine":"italian"},
} 

@app.get("/")
def home():
    return {"message":"Welcome to foodRush"}


@app.get("/restaurants")
def get_restaurant():
    return list(restaruants.values())   

@app.get("/restaurants/{restaruant_id}") 
def get_restaurant(restaruant_id:int):
    restaurant = restaruants.get(restaruant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant
