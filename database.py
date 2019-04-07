"""
    Author : Ashwin Shenoy
    Email : ashwinshenoy05@gmail.com

    This file handles the sqlite database connection. Since a kind of constant check has to be performed on all the houses & bots at all times, the file has to keep running in order to listen to any incoming data at the serial port. 

    A more proper way would be to actually allow the connection to be active and kinda 'sleep' if a certain pre known amount of time has passed. The connection should listen to changes again if activated. 
"""

import sqlite3
import datetime
from serial import Serial

connection = sqlite3.connect("tpsa.db")

ser = Serial(port="\\.\COM3", baudrate=9600)
while True:
    data = ser.readline().decode().strip()
    
    if data == "1":
        print(data)
        connection.execute("INSERT INTO HOUSE_DATA (PUSH_BTN_1, PUSH_BTN_2, PUSH_BTN_3, PUSH_BTN_4, DATE, TIME) \
        VALUES(1, 0, 0, 0, ?, ?)", (datetime.date.today().strftime('%m/%d/%y') , datetime.datetime.now().time().strftime('%H:%M:%S')))
        connection.commit()

    elif data == "2":
        connection.execute("INSERT INTO HOUSE_DATA (PUSH_BTN_1, PUSH_BTN_2, PUSH_BTN_3, PUSH_BTN_4, DATE, TIME) \
        VALUES(0, 1, 0, 0, ?, ?)", (datetime.date.today().strftime('%m/%d/%y') , datetime.datetime.now().time().strftime('%H:%M:%S')))
        connection.commit()

    elif data == "3":
        connection.execute("INSERT INTO HOUSE_DATA (PUSH_BTN_1, PUSH_BTN_2, PUSH_BTN_3, PUSH_BTN_4, DATE, TIME) \
        VALUES(0, 0, 1, 0, ?, ?)", (datetime.date.today().strftime('%m/%d/%y') , datetime.datetime.now().time().strftime('%H:%M:%S')))
        connection.commit()

    elif data == "4":
        connection.execute("INSERT INTO HOUSE_DATA (PUSH_BTN_1, PUSH_BTN_2, PUSH_BTN_3, PUSH_BTN_4, DATE, TIME) \
        VALUES(0, 0, 0, 1, ?, ?)", (datetime.date.today().strftime('%m/%d/%y') , datetime.datetime.now().time().strftime('%H:%M:%S')))
        connection.commit()

    else:
        connection.execute("INSERT INTO HOUSE_DATA (PUSH_BTN_1, PUSH_BTN_2, PUSH_BTN_3, PUSH_BTN_4, DATE, TIME) \
        VALUES(0, 0, 0, 0, ?, ?)", (datetime.date.today().strftime('%m/%d/%y') , datetime.datetime.now().time().strftime('%H:%M:%S')))
        connection.commit()

