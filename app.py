from flask import Flask, render_template, request
from scanner import run_scan, get_open_ports
from analyzer import check_risk
from report import generate_report


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']

    run_scan(target)
    ports = get_open_ports()
    risk = check_risk()

    report_file = generate_report(target, risk, ports)

    return render_template(
        'result.html',
        target=target,
        risk=risk,
        ports=ports,
        report=report_file
    )

if __name__ == "__main__":
    app.run(debug=True)
