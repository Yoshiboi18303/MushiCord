from pymongo import MongoClient
from utils.errors import type_err

def ready_mongo(connection_string):
  connection_string = str(connection_string)
  
  MongoClient(connection_string)

  print(f"Connected to MongoDB!")

async def update_mongo(database_name, collection_name, new_values):
  if database_name is not str(database_name):
    type_err("Duckiot", "String", "Integer or Boolean")
  if collection_name is not str(collection_name):
    type_err("Duckiot", "String", "Integer or Boolean")
  cluster = ready_mongo()
  db = cluster[database_name]
  collection = db[collection_name]

  if new_values.startsWith('{}'):
    post = {new_values}
  else:
    raise SyntaxError("Value: \"new_values\" needs to have {} as the start!")

  collection.insert_one(post)