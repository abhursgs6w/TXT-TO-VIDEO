# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "27153623"))
API_HASH = environ.get("API_HASH", "96f30e285a621f5842b6ba141df964fe")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
