#!/usr/bin/python

from flask import Flask, render_template, request
from flask_cors import CORS
from controller import Controller

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    if request.method == 'POST':
        data = request.json
        input_location = data['location']

        wf = Controller()

        geo_location = wf.getLocation(input_location)
        if geo_location == None:
            wf_address = "Unknown location"
            report_template = render_template('reports.html', weather_address=wf_address)
            return report_template

        wf_address = geo_location.address
        wf_reports = wf.getWeatherReports(data, geo_location)

        report_template = render_template(
            'reports.html', weather_address=wf_address, weather_reports=wf_reports)

    return report_template


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
