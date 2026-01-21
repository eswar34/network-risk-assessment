from flask import Flask, render_template, request, redirect, url_for
from scanner import run_scan, get_open_ports
from analyzer import check_risk
from report import generate_report
import time


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']

    # Start scanning process
    run_scan(target)
    ports = get_open_ports()
    risk = check_risk()

    report_file = generate_report(target, risk, ports)

    # Simulate processing time for better UX
    time.sleep(2)

    return render_template(
        'result.html',
        target=target,
        risk=risk,
        ports=ports,
        report=report_file
    )

@app.route('/loading', methods=['POST'])
def loading():
    target = request.form['target']
    return render_template('loading.html', target=target)

if __name__ == "__main__":
    app.run(debug=True)
