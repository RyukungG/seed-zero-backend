from http.client import HTTPException
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
load_dotenv()

from models import Item

NAME = os.getenv('NAME', default="World")

app = FastAPI()


@app.get("/top-level")
def index():
    return {"message": f"Hello {NAME}"}


@app.get("/calculator/add")
def adder(first_number: int, second_number: int):
    result = first_number + second_number
    return {"first_number": first_number, "second_number": second_number, "result": result}


@app.get("/calculator/substract")
def subtractor(first_number: int, second_number: int):
    result = first_number - second_number
    return {"first_number": first_number, "second_number": second_number, "result": result}


@app.get("/calculator/multiply")
def multiply(first_number: int, second_number: int):
    result = first_number * second_number
    return {"first_number": first_number, "second_number": second_number, "result": result}


@app.get("/calculator/divide")
def divide(first_number: int, second_number: int):
    result = first_number / second_number
    return {"first_number": first_number, "second_number": second_number, "result": result}


@app.get("/userId/{userId}/info")
def usersInfo(userId: int):
    if userId != 9997:
        raise HTTPException(status_code=404, detail="UserId not found.")

    return {
        "id": userId,
        "name": "Safe",
        "surname": "suk",
    }


# {
#   "name": "Book",
#   "price": 123,
# Example Request Body:
# }
# @app.????(???)
@app.post("/item/create/")
def itemCreator(item: Item):
    print(f"name: {item.name}\n"
          f"price: {item.price}")
    return item.name, item.price


