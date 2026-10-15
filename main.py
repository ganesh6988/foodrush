from fastapi import FastAPI

app = FastAPI(title="FoodRush API", version="0.1.0")

@app.get("/")
def root():
    return {"message":"Welcome to FoodRush API"}

@app.get("/health")
def health():
    return {"Status":"ok"}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"product_id":product_id, "name":"sample product"}


@app.get("/search")
def search(q:str, limit:int = 10):
    return {"query":q, "limit":limit} 

from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    price: int = Field(gt=0)
    stock: int = Field(ge=0)

@app.post("/products", status_code=201)
def create_product(data: ProductCreate):
    return {"message": "created", "product": data.model_dump()}
