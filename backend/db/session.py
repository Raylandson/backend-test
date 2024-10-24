from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
# Replace <db_password> with t'he actual password for your admin user
MONGO_URI = f"mongodb+srv://{db_user}:{db_password}@travels.3dckthr.mongodb.net/?retryWrites=true&w=majority"

# You can specify your database name here if you already know it
MONGO_DB = "travels"

# Create the MongoClient and specify the database
client = MongoClient(MONGO_URI,
    connecttimeoutms=60000,
    serverselectiontimeoutms=60000)
db = client[MONGO_DB]

def get_db():
    return db
