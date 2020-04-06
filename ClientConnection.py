import pymongo
import dns

# you will need to change this connection string to match your own instance
#client = pymongo.MongoClient("Get this from Atlas and change <password> to your password (and remove the <>)")
#client = pymongo.MongoClient("mongodb+srv://Mansee:deargeo@clustersmp-s6rtd.azure.mongodb.net/test?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://Mansee:deargeo@clustersmp-s6rtd.azure.mongodb.net/test")

# remember that if you have special characters in your password, you need to "escape" them
# or import and use urllib.parse.quote_plus
# More info: https://pymongo.readthedocs.io/en/stable/examples/authentication.html
# Ascii codes: https://ascii.cl/

mydb = client["sample_airbnb"]
mycollection = mydb["listingsAndReviews"]

# this finds and returns the first document with the field "name" equal to "White House"
mydocument = mycollection.find_one({"name":"White House"})
print(mydocument)