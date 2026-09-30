import datetime
import zoneinfo

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "Welcome"


@app.route("/event/<int:id>")
def event(id):
    name = "Party"
    location = "London"
    guestList = "Riv", "fred","AJ"

    date = datetime.datetime(1966, 9, 11, 18, 30, 0, tzinfo=zoneinfo.ZoneInfo("Europe/London"))

    return render_template(
        "events.html",
        event_name=name,
        event_location=location,
        event_date=date,
        guestList=guestList,
    )


@app.route("/booking/<int:id>")
def booking(id):
    bookingInfo = {
        "id" : id,
        "name": "Rivett",
        "event" : "party",
        "date" :  datetime.datetime(1966, 9, 11, 18, 30, 0, tzinfo=zoneinfo.ZoneInfo("Europe/London")),
        "location" : "3rd floor swimming pool",
        "amountPaid" : 1
    }

    return render_template("booking.html", booking = bookingInfo)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
