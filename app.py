from flask import Flask, render_template, request,abort
from markupsafe import escape
from my_continuityCounter import csvMaker
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/plot', methods = ['POST', 'GET'])
def plot():
    try:
        if request.method == 'GET':
            dateRange = {'startDate':"2021-01-01", 'endDate':"2021-12-01"}
            csvMaker(pd.read_csv("worker_activity.csv"), dateRange)
        if request.method == 'POST':
            form_data = request.form
            print(form_data)
            csvMaker(pd.read_csv("worker_activity.csv"), form_data)
        data = pd.read_csv("result.csv")
        results = pd.DataFrame(data)
        continuityFrequency = results.value_counts('Continuity')
        x = continuityFrequency.index
        y = continuityFrequency.values
        totalWorkers= len(results)
        avgContinuity= round(results["Continuity"].mean(),2)
        highestContinuity= results["Continuity"].max()
        minContinuity = results["Continuity"].min()
        greaterThanOne= len(results[(results['Continuity'] > 1)])
        plt.bar(x, y, color=['blue'])
        plt.ylabel('Frequency of Continuity')
        plt.xlabel('Continuity')
        plt.title('Continuity of Workers')
        plt.savefig('static/images/continuityworker.png')

        return render_template('continuityworker.html', url='/static/images/continuityworker.png', totalWorkers = totalWorkers,
        avgContinuity = avgContinuity, highestContinuity = highestContinuity, minContinuity= minContinuity,
        greaterThanOne = greaterThanOne)
    except IndexError: 
        abort(404)

@app.route("/csv")
def csv():
    data = pd.read_csv("result.csv")
    results = pd.DataFrame(data)
    return render_template('data.html',  tables=[results.to_html(classes='data')], titles=results.columns.values)
if __name__ == '__main__':
   app.run()  

# @app.route('/about_project/')
# def about():
#     return '<h3> This page is about the project </h3>'

# @app.route('/users/<int:user_id>')
# def greet_user(user_id):
#     users = ['Karley', 'George']
#     try:
#         return'<h2> hi {} </h2>'.format(users[user_id])
#     except IndexError: 
#         abort(404)


# @app.route('/plot')
# def plot():
#     left = [1, 2, 3, 4, 5]
#     # heights of bars
#     height = [10, 24, 36, 40, 5]
#     # labels for bars
#     tick_label = ['one', 'two', 'three', 'four', 'five']
#     # plotting a bar chart
#     plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

#     # naming the y-axis
#     plt.ylabel('y - axis')
#     # naming the x-axis
#     plt.xlabel('x - axis')
#     # plot title
#     plt.title('My bar chart!')

#     plt.savefig('static/images/plot.png')

#     return render_template('plot.html', url='/static/images/plot.png')

# if __name__ == '__main__':
#    app.run()  


   