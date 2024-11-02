from fastapi import FastAPI, Response, Cookie
import string
import random

app = FastAPI()


@app.get("/set_cookie")
def set_cookie(response: Response):
    response.set_cookie(
        key="special_cookie",
        value="".join(
            random.choices(string.ascii_letters, k=26)
        ),  # "random" string sequence
    )
    return {"message": "Cookie now set!"}


@app.get("/get_cookie")
def get_cookie(special_cookie: str = Cookie(None)):
    return {"special_cookie": special_cookie}  # returns cookie value
