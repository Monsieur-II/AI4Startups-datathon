from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Any

import uvicorn

from Dtos.customer import Customer
from helper import get_recommendations_image_pair

app = FastAPI (title="Afrimash Api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=["http://localhost:8080", "http://localhost:8081", "http://127.0.0.1:5173", "https://011d69331104.ngrok-free.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

default_image_url = "http://example.com/default_product.jpg"


@app.post("/api/v1/recommendations")
def get_recommendations(payload: Customer) -> Any:
    print(payload)
    result = get_recommendations_image_pair(customer_id=payload.customerId)
    print(result)
    payload_list = [
    {
        "title": item["Product_Name"],
        "image_url": f"{item['Image_URL']}"
    }
    for item in result]
    return payload_list

@app.post("/api/v1/new-customer")
def get_recommendations() -> Any:
    result = get_recommendations_image_pair("CUSD001")
    payload_list = [
    {
        "title": item["Product_Name"],
        "image_url": f"{item['Image_URL']}"
    }
    for item in result]
    return payload_list


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
