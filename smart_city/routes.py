from flask import render_template
from smart_city import smart_city

@smart_city.route("/")
@smart_city.route("/home")
def home():
    return render_template("base.html")

smart_city.run(debug=True)