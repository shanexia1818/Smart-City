import json
from firebase_admin import db
from .camera import VideoCamera
from smart_city import smart_city
from flask import render_template, Response

@smart_city.route("/")
@smart_city.route("/home")
def home():
    return render_template("home_page_housing.html")


@smart_city.route("/bots")
def bots():
    return render_template("home_page_bots.html")


@smart_city.route("/smart-house")
def smart_house():
	"""
	This route connects to the page that displays all the push button events fired from the smart house. 
	"""
	# smart_city_data = sqlite3.connect("./tpsa.db")
	# house_data = smart_city_data.cursor().execute("SELECT id, push_btn_1, push_btn_2, push_btn_3, push_btn_4, date, time FROM HOUSE_DATA")
	# data = []
	# for row in house_data:
	# 	stored_data = {
	# 		"id": row[0],
	# 		"push_btn_1": row[1],
	# 		"push_btn_2": row[2],
	# 		"push_btn_3": row[3],
	# 		"push_btn_4": row[4],
	# 		"date": row[5],
	# 		"time": row[6]
	# 	}
	# 	data.append(stored_data)
	data = db.reference("house").get()
	return render_template("house.html", data=data)


@smart_city.route("/smart-hospital")
def smart_hospital():
    return render_template("hospital.html")


@smart_city.route("/smart-mall")
def smart_mall():
    return render_template("mall.html")


@smart_city.route("/smart-school")
def smart_school():
    return render_template("school.html")


@smart_city.route("/live_feed")
def live_feed():
    return render_template("webcam_feed.html")


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@smart_city.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


smart_city.run(debug=True)