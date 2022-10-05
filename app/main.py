from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Header

TOKEN = "MzM3NDY3NjUzMjc0Oji1wxU5T7SsWdfFUa5AiECBxMeJ"

from app.db import engineOracle

class customQuery(BaseModel):
    query: str = None

app = FastAPI()

@app.post("/")
async def oracleCustomQuery(query: customQuery, Authorization: Union[str, None] = Header(default=None)):
    if Authorization == "Bearer " + TOKEN:
      data = engineOracle.execute(query.query).fetchall()
      return data
    else:
      return {"Authorization": "You don't have permission"}