from fastapi import FastAPI
from router import router

import re

app = FastAPI()
app.include_router(router, prefix="/books/ORM")


@app.get("/")
async def hello():
    return {"response": 400}


@app.get("/number/")
async def get_number(text: str):
    # test = " ASDFASD +380953569756 +38 0 (50) 35697-56 asdf adf"
    pattern = (
        r"((?:\+?)(?:38?)(?:| |-)0(?:| |-)(?:\(?)(?:50|95|99)(?:\)?)"
        r"(?:| |-)(?:[0-9]{3})(?:| |-)(?:[0-9]{2})(?:| |-)(?:[0-9]{2}))"
    )
    result = re.findall(pattern, text)
    return {"response": result}
