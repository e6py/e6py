from os import environ as env

from dotenv import load_dotenv

from e6py.http.client import HTTPClient

load_dotenv()


class Client(HTTPClient):
    BASE = env.get("URL")


client = Client(login=env.get("USER"), api_key=env.get("KEY"))
