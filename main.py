from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.get('/items/')
async def create_item(
        q: Annotated[
            list[str] | None,
            Query(
                alias="item-query",
                title="Query string",
                description="Query string for the items to search in the database that have a good match",
                min_length=3,
                max_length=50,
                regex="^fixedquery$",
                deprecated=True,
            )] = None
) -> dict:
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result |= {"q": q}
    return result
