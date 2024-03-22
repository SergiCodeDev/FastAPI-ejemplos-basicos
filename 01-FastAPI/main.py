# uvicorn main:app --reload
# correr servidor

from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Web FastAPI"}

 

# declarar antes las rutas fijas que las que puedes enviar algo como objeto/{id}

@app.get("/objeto/me")
async def read_user_me():
    return {"user_id": "the current user"}

# hay que tipar las variables para la documentacion y autocompletado ej: id: int,id: str,id: float, id: bool

@app.get("/objeto/{id}")
async def dar_id(id: int):
    return {"devolver": id}


class Nombres(str, Enum):
    alexnet = "alexnet2"
    resnet = "resnet2"
    lenet = "lenet2"

# le das el valor en el naveador

@app.get("/nombre/{clave}")
async def obtener_nombre_usuario(clave: Nombres):
    if clave is Nombres.alexnet:
        return {"clave": clave, "message": "Deep Learning FTW!"}

    if clave.value == "lenet":
        return {"clave": clave, "message": "LeCNN all the images"}

    return {"clave": clave, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

from typing import Union

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item