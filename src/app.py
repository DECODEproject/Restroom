from fastapi import FastAPI
from pydantic import BaseModel
from zenroom.zenroom import zencode_exec

app = FastAPI()


class Result(BaseModel):
    ERR: str
    OUT: str


@app.get("/")
async def root(zencode: str, data: str, keys: str):
    result = zencode_exec(script=zencode,
                          keys=keys,
                          data=data)

    return result