from odmantic import Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    # class Config:
    #     collection = "books"

    # TypeError: field Config is defined without type annotation