import pandas as pd
from datetime import datetime, date


def formatDate (dateStr):
    return datetime.strptime(dateStr[0:19], '%Y-%m-%d %H:%M:%S')

def organiseData (data,dateRange):
    startDate = data[(data['Date'] >= dateRange['startDate']) & (data['Date'] <= dateRange['endDate'])]
    return startDate.sort_values(['Worker', 'Date'])

def continuityCounter (data):
    continityCount=0
    previousDay = formatDate(data.iloc[0]['Date'])
    previousRole = data.iloc[0]['Role']
    previousEmployer = data.iloc[0]['Employer']
    dayCount=0
    for i, row in data.iterrows(): 
        currentDate = formatDate(row['Date'])
        dayDifference = (((previousDay - currentDate).days)*-1)
        currentRole = row['Role']
        currentEmployer = row['Employer']
        if dayDifference > 6:
            continityCount = 1
            previousDay = currentDate
            continue
        elif previousRole != currentRole:
            continityCount = 1
            previousRole = currentRole
            continue
        elif previousEmployer != currentEmployer: 
            continityCount = 1
            previousEmployer = currentEmployer
            continue
        else:
            continityCount += 1
            previousDay = currentDate
            previousEmployer = currentEmployer
            previousRole = currentRole
    return continityCount

def groupWorker (data,dateRange):
    organisedData = organiseData(data,dateRange)
    print(organisedData)
    previousWorkerId = organisedData.iloc[0]['Worker']
    results = []
    for i, row in organisedData.iterrows():
        currentWorkerId = row['Worker']
        if previousWorkerId == organisedData.iloc[-1]['Worker']:
            workerData = organisedData[organisedData['Worker'] == previousWorkerId]
            results.append([previousWorkerId, continuityCounter(workerData)])
            return results
        if previousWorkerId != currentWorkerId:
            workerData =organisedData[organisedData['Worker'] == previousWorkerId]
            results.append([previousWorkerId, continuityCounter(workerData)])
            previousWorkerId = row['Worker']
    return results

def csvMaker (data,dateRange):
    results = groupWorker(data,dateRange)
    dfResults= pd.DataFrame(results, columns= ['Worker','Continuity'])

    dfResults.to_csv('result.csv', header = ['Worker','Continuity'], index=False)




