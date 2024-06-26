import pymongo

# Establish a connection to the MongoDB server
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the database
mydb = myclient["mydatabase"]

# Select the collection
mycol = mydb["customers"]

# Function to insert one document
def insert_one_document():
    mydict = {"name": "John", "address": "Highway 37"}
    x = mycol.insert_one(mydict)
    print("Inserted one document with _id:", x.inserted_id)

# Function to insert multiple documents
def insert_many_documents():
    mylist = [
        {"name": "Amy", "address": "Apple st 652"},
        {"name": "Hannah", "address": "Mountain 21"},
        {"name": "Michael", "address": "Valley 345"},
        {"name": "Sandy", "address": "Ocean blvd 2"},
        {"name": "Betty", "address": "Green Grass 1"},
        {"name": "Richard", "address": "Sky st 331"},
        {"name": "Susan", "address": "One way 98"},
        {"name": "Vicky", "address": "Yellow Garden 2"},
        {"name": "Ben", "address": "Park Lane 38"},
        {"name": "William", "address": "Central st 954"},
        {"name": "Chuck", "address": "Main Road 989"},
        {"name": "Viola", "address": "Sideway 1633"}
    ]
    x = mycol.insert_many(mylist)
    print("Inserted multiple documents with _ids:", x.inserted_ids)

# Function to insert multiple documents with specified IDs
def insert_many_documents_with_ids():
    mylist = [
        {"_id": 1, "name": "John", "address": "Highway 37"},
        {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
        {"_id": 3, "name": "Amy", "address": "Apple st 652"},
        {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
        {"_id": 5, "name": "Michael", "address": "Valley 345"},
        {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
        {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
        {"_id": 8, "name": "Richard", "address": "Sky st 331"},
        {"_id": 9, "name": "Susan", "address": "One way 98"},
        {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
        {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
        {"_id": 12, "name": "William", "address": "Central st 954"},
        {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
        {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
    ]
    x = mycol.insert_many(mylist)
    print("Inserted multiple documents with specified _ids:", x.inserted_ids)

# Main function to execute the insertions
if __name__ == "__main__":
    insert_one_document()
    insert_many_documents()
    insert_many_documents_with_ids()
