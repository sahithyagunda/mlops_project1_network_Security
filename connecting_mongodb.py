
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://gundasahithya908:DI5I4ZxrhDkzB2Du@mlopscluster.shzqjhm.mongodb.net/?retryWrites=true&w=majority&appName=mlopscluster"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)