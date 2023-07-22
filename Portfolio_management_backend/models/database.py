from pymongo import MongoClient
client = MongoClient('mongodb+srv://madhuamoli16:mahi@cluster0.ryl0jye.mongodb.net/?retryWrites=true&w=majority')
db = client['Portfolio_XTR_Management']
user = db['users']
projects=db['projects']
tasks=db['tasks']
resource=db['resources']
activeUser=db['activeUser']
count=db['counter']