from enum import Enum

from fastapi import FastAPI

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int,
        item_id: str,
        q: str | None = None,
        short: bool = False
) -> dict:
    item = {'item_id': item_id, 'owner_id': user_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {'description': 'This is an amazing item that has a long description'}
        )
    return item


@app.get('/items/{item_id}')
async def get_item(item_id: str, needy: str, skip: int = 0, limit: int = 10) -> dict:
    item = {'item_id': item_id, 'needy': needy, 'skip': skip, 'limit': limit}
    item.update(fake_items_db[0])
    return item
