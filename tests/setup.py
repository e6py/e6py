from os import environ as env

from e6py.http.client import HTTPClient

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Client(HTTPClient):
    BASE = env.get("URL")


client = Client(login=env.get("USER"), api_key=env.get("KEY"))
