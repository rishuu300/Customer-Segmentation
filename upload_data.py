from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://rishuu300:Rishurock300@cluster0.48xo5og.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Database and cluster
DATABASE_NAME = "Customer_Segmentation"
COLLECTION_NAME = "customer_segmentation"

df = pd.read_csv(
    "C:\\Users\\91808\Documents\\PW\\6. Machine Learning\\15. Projects\\2. Customer Segmentation\\notebooks\\marketing_campaign.csv",
    sep="\t"
)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
