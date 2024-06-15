from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def work_breakdown_structure():  # put application's code here
    return render_template('workbreakdownstructure.html')

@app.route('/networkactivitydiagram')
def network_activity_diagram():
    return render_template('networkactivitydiagram.html')

@app.route('/riskbreakdownstructure')
def risk_breakdown_structure():
    return render_template('riskbreakdownstructure.html')

@app.route('/hrmsganttchart')
def HRMSGanttChart():
    return render_template('hrmsganttchart.html')

@app.route('/kanbanchart')
def kanban_chart():
    return render_template('kanbanchart.html')


if __name__ == '__main__':
    app.run()
