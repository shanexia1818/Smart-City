"""
    Author : Ashwin Shenoy
    Email : ashwinshenoy05@gmail.com

    This file handles the sqlite database connection. Since a kind of constant check has to be performed on all the houses & bots at all times, the file has to keep running in order to listen to any incoming data at the serial port. 

    A more proper way would be to actually allow the connection to be active and kinda 'sleep' if a certain pre known amount of time has passed. The connection should listen to changes again if activated. 
"""

import sqlite3
import datetime
import paho.mqtt.client as mqtt 

connection = sqlite3.connect("tpsa.db")

bots_called = ['garbage']
def on_connect(client, userdata, flags, rc): 
   print("Connected with result code " + str(rc)) 
   client.subscribe("Building/Apartment")	
	

def on_message(client, userdata, msg):
	print(bots_called)
	data = str(msg.payload.decode('utf-8'))
    bots_called.append(data)
    if (bots_called[len(bots_called) - 1] != data):
        connection.execute("INSERT INTO HOUSE_DATA (PUSH_BTN_1, PUSH_BTN_2, PUSH_BTN_3, PUSH_BTN_4, DATE, TIME) \
            VALUES(1, 0, 0, 0, ?, ?)", (datetime.date.today().strftime('%m/%d/%y') , datetime.datetime.now().time().strftime('%H:%M:%S')))
            connection.commit()
    else:
        print("Nothing")
	print('-----------------')

client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 
client.connect('test.mosquitto.org', 1883, 60) 

client.loop_start()

while True:
	client.subscribe("Building/Apartment")
	time.sleep(1)

