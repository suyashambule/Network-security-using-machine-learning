import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the MongoDB URI from the environment variable
uri = os.getenv("MONGO_DB_URI")

if not uri:
    print("MongoDB URI not found in the .env file")
else:
    # Create a new client and connect to the server
    client = MongoClient(uri)

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print("Error occurred while connecting to MongoDB:", e)
