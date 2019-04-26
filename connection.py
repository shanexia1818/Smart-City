import json
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("smart_city_database_secret.json")

firebase_admin.initialize_app(cred, options={
    "databaseURL": "https://smart-city-61e3d.firebaseio.com"
})

ref = db.reference("house")
data = ref.set({
    "button_5": 0
})

print(ref.get())