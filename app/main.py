from typing import Annotated, Any

import orjson
from fastapi import Body, FastAPI, HTTPException
from fastapi.responses import PlainTextResponse

import data

current_kv = data.seed_kv_data()
app = FastAPI()


@app.get("/", response_class=PlainTextResponse)  # zone apex
def root():
    return "rootv20240409"


@app.get("/kv/{key}")
async def get_kv(key: str) -> Any:
    if key in current_kv:
        return current_kv[key]

    raise HTTPException(status_code=404, detail="Key not found")


@app.post("/kv/{key}")
async def set_kv(key: str, value: Annotated[dict, Body()]) -> None:
    current_kv[key] = value


@app.get("/csv", response_class=PlainTextResponse)
async def get_generated_csv(numrows: int = 1, numcols: int = 1) -> str:
    return data.generate_csv_data(numrows, numcols)
