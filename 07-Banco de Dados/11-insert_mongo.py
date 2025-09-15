from pymongo import MongoClient

client = MongoClient()
mydb = client.dbposts
mycol = mydb.posts

post1 = {
    "title": "Organization",
    "category": "Production",
    "level": "Intermediário",
    "author": {
        "name": "Priscila",
        "email": "priscila.moreton16@email.com"
    }
}

result = mycol.insert_one(post1)
print("Documento incluído com sucesso")