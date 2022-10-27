import firebase_admin
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate("test-a2355-firebase-adminsdk-ntifn-9c1cc6cd30.json")
app = firebase_admin.initialize_app(cred)
# Application Default credentials are automatically created.

db = firestore.client()


users_ref = db.collection('utenti')
docs = users_ref.stream()

doc_ref = db.collection(u'utenti').document(u'alovelace')
doc_ref.set({
    u'nome': u'Alan',
    u'secondonome': u'Mathison',
    u'cognome': u'Ferro',
    u'data': 1912
})


 

for doc in docs:
    print(doc.to_dict()['nome'])
    #print(f'{doc.id} => {doc.to_dict()}')
print('---------')
cities_ref = db.collection("utenti")
query = cities_ref.where("nome", u'==', 'Simo').limit(4)
results = query.get()

for doc in results:
    print(doc.to_dict()['nome'])