from pymongo import MongoClient

import json
with open("/home/namruthapallerla/kent/dataweb/private.json","r") as f:
    private = json.load(f)

password = private["mongo"]



client = pymongo.MongoClient("mongodb+srv://namrutha:{password}@soliton1.knniwga.mongodb.net/?retryWrites=true&w=majority")




from bson.objectid import ObjectId

shopping_db = client.shopping_db
list_collection = shopping_db.list_collection

list_collection.delete_many({})

list_collection.insert_many([
        { "description": 'apples' },
        { "description": 'broccoli' },
        { "description": 'pizza' },
        { "description": 'tangerine' },
        { "description": 'potatoes' }
    ])

items = list(list_collection.find())
print(items)