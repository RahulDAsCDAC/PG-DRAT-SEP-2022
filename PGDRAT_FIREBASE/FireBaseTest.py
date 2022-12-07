import firebase_admin   # pyrebase5
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
"""
# Add/Set Data
# Add Document With Unknown ID
data = {
    'name':"Ravi Sankar",
    'age': 33,
    'employed':True,
}
db.collection('users').add(data)

# Set Document With Known ID
data = {
    'name':'Person 1',
    'age':40,
    'employed':False,
}

db.collection('users').document('#002').set(data)

# Nested Collection
db.collection('users').document('#002').collection('Movies').document('movie001').set({
    'name':['Avengers', 'DDLJ', 'SNWH'],
})

# Read Data
# Reading A Document With Known ID
result = db.collection('users').document('#003').get()
if result.exists:
    print(result.to_dict())
else:
    print("There is no data related to your query!")

# Get All Documents In A Collection
docs = db.collection('users').get()
for doc in docs:
    print(doc.to_dict())

# Query Using Properties
docs = db.collection('users').where('age','==',33).get()
for doc in docs:
    print(doc.to_dict())

# Update Data
# Update Data With Known ID
db.collection('users').document('#002').update({'name':'Sanjib'})
db.collection('users').document('#002').update({'age':35, 'employed':True})
db.collection('users').document('#002').update({'address':{
    'city':'Kolkat',
    'state':'West Bengal',
},
'mother_toungue':'Bengal',
})
db.collection('users').document('#002').update({'language':['Bengali','Hindi','English','Sanskrit']})
db.collection('users').document('#002').update({'language':firestore.ArrayUnion(['Japanese'])})
db.collection('users').document('#002').update({'language':firestore.ArrayRemove(['Japanese'])})

# Delete Data
# Delete Data With Known ID
db.collection('users').document('#002').delete()

# Delete Field With Known ID
db.collection('users').document('#001').update({'married':firestore.DELETE_FIELD})
"""