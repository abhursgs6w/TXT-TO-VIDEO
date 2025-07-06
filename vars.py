# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "27355640"))
API_HASH = environ.get("API_HASH", "ec8cdb234c7bd12d930c2649023be1b4")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
