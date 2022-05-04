import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns




def plot():

    data = pd.read_csv("result.csv")
    results = pd.DataFrame(data)
    continuityFrequency = results.value_counts('Continuity')
    x= continuityFrequency.index
    y = continuityFrequency.values
    plt.bar(x, y, color=['blue'])
    plt.ylabel('Frequency of Continuity')
    plt.xlabel('Continuity')
    plt.title('Continuity of Workers')
    plt.show()
    plt.savefig('static/images/continuityworker.png')

plot()

def statements ():
    data = pd.read_csv("result.csv")
    results = pd.DataFrame(data)
    totalWorkers= len(results)
    avgContinuity= round(results["Continuity"].mean(),2)
    highestContinuity= results["Continuity"].max()
    minContinuity = results["Continuity"].min()
    greaterThanOne= len(results[(results['Continuity'] > 1)])
    print(f"""Total workers: {totalWorkers}""")
    print(f"""Average Continuity: {avgContinuity}""")
    print(f"""Maximum Continuity: {highestContinuity}""")
    print(f"""Min Continuity: {minContinuity}""")
    print(f"""Continuity Greater Than One: {greaterThanOne}""")
statements()

# data = pd.read_csv("result.csv")
# results = pd.DataFrame(data)
# continuity = results['Continuity']
# worker = results['Continuity'].value_counts()
# print(worker)