from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.models import mongodb

from app.models.book import BookModel

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    book = BookModel(keyword="파이썬", publisher="BJPublic", price=1200, image="me.png", hhh="askljdlkas")
    print(await mongodb.engine.save(book))  # DB에 저장
    print("확인")
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "콜렉터 북북이"}
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    print("체크")
    return templates.TemplateResponse(
        "./index.html", {"request": request, "title": "콜렉터 북북이", "keyword": q}
    )


@app.on_event("startup")
def on_app_start():
    """before app starts"""
    mongodb.connect()


@app.on_event("shutdown")
def on_app_shutdown():
    print("bye server")
    """after app shutdown"""
    # netstat -ano
    # taskkill /f /pid num
    mongodb.close()


# from enum import Enum

# from fastapi import FastAPI


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# app = FastAPI()


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.lenet.value:
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}


# from typing import Optional
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/hell")
# async def root():
#     print("hello")
#     return {"message": "Hello World"}


# # @app.get("/items/{item_id}")
# # async def read_item(item_id):
# #     return {"item_id": item_id}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


# @app.get("/items/{item_id}/{asd}")
# async def root(item_id: int, asd: str, q: Optional[str] = None):
#     return {"item_id": item_id, "asd": asd, "q": q}


# from typing import Optional

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}

# @app.get("/item/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
