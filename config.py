
from turtle import clear
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import motor.motor_asyncio
import os
import time
from pymongo import MongoClient

# ----------------- Database variables (MongoDB) --------------------------
# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])
# db = client.myTestDB
try:
    conn = MongoClient('localhost',27017)
    print("Connected successfully!!!")
except:  
    print("Could not connect to MongoDB")

cl = conn.get_database('ELYDATA')
db= cl['Scraper']     
