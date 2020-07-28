import firebase_admin
from firebase_admin import credentials, firestore
import google.cloud

cred = credentials.Certificate('home-automation.json')
firebase_admin.initialize_app(cred)

store = firestore.client()
#doc_ref = store.collection(u'users').limit(2)

#try:
 #   docs = doc_ref.get()
 #   for doc in docs:
  #      print(u'Doc Data:{}'.format(doc.to_dict()))
#except google.cloud.exceptions.NotFound:
 #   print(u'Missing data')


doc_ref = store.collection(u'face-recognition')
doc_ref.add({u'name': u'test', u'added': u'just now'})

