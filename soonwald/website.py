
from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page_title="Soonwald Festival")

@app.route('/merch')
def merch():
    return render_template('merch.html', page_title="Merch - Soonwald Festival")

@app.route('/timetable')
def timetable():
    return render_template('timetable.html', page_title="Timetable - Soonwald Festival")

@app.route('/bar')
def bar():
    return render_template('bar.html', page_title="Bar - Soonwald Festival")

@app.route('/activities')
def activities():
    return render_template('activities.html', page_title="Activities - Soonwald Festival")

@app.route('/tickets')
def tickets():
    return render_template('tickets.html', page_title="Tickets - Soonwald Festival")

@app.route('/soonpay')
def soonpay():
    return render_template('soonpay.html', page_title="Soonpay - Soonwald Festival")

@app.route('/archiv')
def archiv():
    return render_template('archiv.html', page_title="Archiv - Soonwald Festival")


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
