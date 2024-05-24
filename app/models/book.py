from odmantic import Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    img: str

    class Config:
        collection = "books"


# db fastapi-pj -> collection books -> document {}
