import time 
import firebase_admin
import paho.mqtt.client as mqtt 
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./smart_city_database_secret.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

bots_called = ['garbage']
def on_connect(client, userdata, flags, rc): 
   print("Connected with result code " + str(rc)) 
   client.subscribe("Building/Apartment")	
	

def on_message(client, userdata, msg):
	print(bots_called)
	data = str(msg.payload.decode('utf-8'))
	bots_called.append(data)
	print(bots_called[len(bots_called) - 1])
	# if (bots_called[len(bots_called) - 1] == data):
	doc_ref = db.collection(u'apartment').document(u'{}'.format(data))
	doc_ref.set({
		u'first': u'Ada'
	})
	# else:
	# 	print("Nothing")
	print(data) 
	print('-----------------')

client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 
client.connect('test.mosquitto.org', 1883, 60) 

client.loop_start()

while True:
	client.subscribe("Building/Apartment")
	time.sleep(1)
