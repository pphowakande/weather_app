#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, render_template, request
from flask_cors import CORS
from controller import EZWController

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/ezw', methods=['POST', 'GET'])
def ezw():
    if request.method == 'POST':
        data = request.json
        input_location = data['location']
        print("input_location : ", input_location)

        ezw = EZWController()

        geo_location = ezw.getLocation(input_location)
        print("geo_location : ", geo_location)
        if geo_location == None:
            ezw_address = "Unknown location"
            report_template = render_template('reports.html', weather_address=ezw_address)
            return report_template

        ezw_address = geo_location.address
        print("ezw_address : ", ezw_address)
        ezw_reports = ezw.getWeatherReports(data, geo_location)
        print("ezw_reports : ", ezw_reports)

        # for report in ezw_reports:
        # 	print("report : ",report)
        # 	print("report.date : ", report.date)
        # 	print("report.max_temperature : ", report.max_temperature)
        # 	print("report.min_temperature : ", report.min_temperature)
        # 	print("report.summary : ", report.summary)

        report_template = render_template(
            'reports.html', weather_address=ezw_address, weather_reports=ezw_reports)

        print("report_template : ", report_template)
    print("return----------------")
    return report_template


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
