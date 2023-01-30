from djangoapp.analytics.l_normalizer import LNormalizer
from sklearn import svm
from djangoapp.models import Temperature, Humidity, Pressure
import pandas as pd
import numpy as np
import base64
from io import BytesIO
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from datetime import datetime
from matplotlib import pyplot

def get_graph():
    buffer = BytesIO()
    pyplot.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_chart(key1, key2, chart_type, data, color='gray'):
    pyplot.switch_backend('AGG')
    fig = pyplot.figure(figsize=(12, 6))
    pyplot.xticks(rotation=90)
    pyplot.grid(True)
    d = data.groupby(key1, as_index=False)[key2].agg('mean')

    if chart_type == 'bar_graph':
        pyplot.bar(d[key1], d[key2], color=color)
        pyplot.xlabel(key1)
        pyplot.ylabel(key2)
    elif chart_type == 'pie_chart':
        pyplot.pie(data=d, x=key2, labels=d[key1])
    elif chart_type == 'line_graph':
        pyplot.plot(d[key1], d[key2], color=color, marker='o', linestyle='dashed')
        pyplot.xlabel(key1)
        pyplot.ylabel(key2)
    else:
        print("Apparently...chart_type not identified")
    pyplot.tight_layout()
    chart = get_graph()
    return chart

class Analytics:

    def get_temperatureBarGraph(self):
        return get_chart('date', 'temperature', 'bar_graph', self.temperatureSeries, '#1a7a81')

    def get_humidityBarGraph(self):
        return get_chart('date', 'humidity', 'bar_graph', self.humiditySeries, '#5EBEC4')

    def get_pressureLineGraph(self):
        return get_chart('date', 'pressure', 'line_graph', self.pressureSeries, '#460d25')

    def get_correlationTempPrLineGraph(self):
        return get_chart('temperature', 'pressure', 'line_graph', self.getCorellationFrameTemp(), '#F92C85')

    def get_correlationHumTempLineGraph(self):
        return get_chart('humidity', 'temperature', 'line_graph', self.getCorellationFrameHum(), '#5EBEC4')

    def get_correlationPrHumLineGraph(self):
        return get_chart('pressure', 'humidity', 'line_graph', self.getCorellationFramePr(), '#460d25')

    def get_humidityHtml(self):
        x1 = self.humidityMean.groupby('date', as_index=False)['humidity'].mean()
        x1['humidity'] = x1["humidity"].round(1).apply(str)
        return x1.to_html(classes='table table-striped')

    def get_pressureHtml(self):
        x1 = self.pressureMean.groupby('date', as_index=False)['pressure'].mean()
        x1['pressure'] = x1["pressure"].round(1).apply(str)
        return x1.to_html(classes='table table-striped')

    def get_temperatureHtml(self):
        x1 = self.temperatureMean.groupby('date', as_index=False)['temperature'].mean()
        x1['temperature'] = x1["temperature"].round(1).apply(str)
        return x1.to_html(classes='table table-striped')

    def __init__(self):

        tempVal = []
        tempMeanData =[]
        tempData = []
        humVal = []
        humData = []
        humMeanData = []
        pressVal = []
        pressData = []
        pressMeanData = []

        for hum in Humidity.objects.all():
            humData.append(self.dateTimeFormatter(hum.dateTime))
            humMeanData.append(self.dateTimeFormatterMean(hum.dateTime))
            humVal.append(hum.humidity)
            self.humidityMean = pd.DataFrame({
                'date': pd.Series(humMeanData),
                'humidity': pd.Series(humVal)
            })
            self.humiditySeries = pd.DataFrame({
                'date': pd.Series(humData),
                'humidity': pd.Series(humVal)
            })

        for press in Pressure.objects.all():
            pressData.append(self.dateTimeFormatter(press.dateTime))
            pressMeanData.append(self.dateTimeFormatterMean(press.dateTime))
            pressVal.append(press.pressure)
            self.pressureMean = pd.DataFrame({
                'date': pd.Series(pressMeanData),
                'pressure': pd.Series(pressVal)
            })
            self.pressureSeries = pd.DataFrame({
                'date': pd.Series(pressData),
                'pressure': pd.Series(pressVal)
            })

        for temp in Temperature.objects.all():
            tempData.append(self.dateTimeFormatter(temp.dateTime))
            tempVal.append(temp.temperature)
            tempMeanData.append(self.dateTimeFormatterMean(temp.dateTime))

            self.temperatureMean = pd.DataFrame({
                'date': pd.Series(tempMeanData),
                'temperature': pd.Series(tempVal)
            })
            self.temperatureSeries = pd.DataFrame({
                'date': pd.Series(tempData),
                'temperature': pd.Series(tempVal)
            })

    def getTestDataTemp(self):
        temp = self.getCorellationFrameTemp()
        Y = temp['temperature']
        X = temp.drop('temperature', axis=1)
        print(X)
        X_train, X_test, y_train, y_test = train_test_split(
            X, Y, test_size=0.25, random_state=143)

        lnorm_transf = LNormalizer()
        skl_pipeline = Pipeline(
            steps=[('normalizer', lnorm_transf), ('regression_estimator', LinearRegression())])
        skl_pipeline.fit(X_train.loc[:, ['date', 'pressure']].values, y_train)
        y_pred_temp = skl_pipeline.predict(
            X_test.loc[:, ['date', 'pressure']].values)
        rmse_temp = np.mean((np.round(y_pred_temp) - y_test.values)**2)**0.5
        print('Середнєквадратичне відхилення: {}'.format(rmse_temp))
        return y_pred_temp, rmse_temp

    def getCorellationFrameTemp(self):
        temperatureObj = []
        pressureObj = []
        base_time = None
        base_time_press = None

        for temp in Temperature.objects.all():
            time = temp.dateTime
            newTime = datetime(time.year, time.month,
                               time.day, time.hour, time.minute, time.second, 0)
            if base_time is None:
                base_time = datetime(time.year, time.month,
                                     time.day-1, 0, 0, 0, 0)
            timedelta = pd.Timedelta(newTime - base_time).total_seconds()//60
            temperatureObj.append(CorellationModel(
                float(temp.temperature), int(timedelta)))

        for press in Pressure.objects.all():
            time = press.dateTime
            newTime = datetime(time.year, time.month,
                               time.day, time.hour, time.minute, time.second, 0)
            if base_time_press is None:
                base_time_press = datetime(
                    time.year, time.month, time.day-1, 0, 0, 0, 0)
            timedelta = pd.Timedelta(
                newTime - base_time_press).total_seconds()//60
            pressureObj.append(CorellationModel(
                float(press.pressure), int(timedelta)))

        tempList = []
        pressList = []
        dateList = []
        for pr in pressureObj:
            if pr.time in dateList:
                continue
            for temp in temperatureObj:
                if (pr.time == temp.time):
                    tempList.append(temp.value)
                    pressList.append(pr.value)
                    dateList.append(pr.time)
                    temperatureObj.remove(temp)
                    break
        print(tempList)
        print(pressList)
        print(dateList)
        return pd.DataFrame(
            {
                'date': dateList,
                'pressure': pressList,
                'temperature': tempList
            }
        )

    def getTestDataHum(self):
        hum = self.getCorellationFrameHum()
        Y = hum['humidity']
        X = hum.drop('humidity', axis=1)
        print(X)
        X_train, X_test, y_train, y_test = train_test_split(
            X, Y, test_size=0.25, random_state=143)

        lnorm_transf = LNormalizer()
        skl_pipeline = Pipeline(
            steps=[('normalizer', lnorm_transf), ('regression_estimator', LinearRegression())])
        skl_pipeline.fit(X_train.loc[:, ['date', 'temperature']].values, y_train)
        y_pred_hum = skl_pipeline.predict(
            X_test.loc[:, ['date', 'temperature']].values)
        rmse_hum = np.mean((np.round(y_pred_hum) - y_test.values)**2)**0.5
        print('Середнєквадратичне відхилення: {}'.format(rmse_hum))
        return y_pred_hum, rmse_hum

    def getCorellationFrameHum(self):
        humidityObj = []
        temperatureObj = []
        base_time = None
        base_time_temp = None

        for hum in Humidity.objects.all():
            time = hum.dateTime
            newTime = datetime(time.year, time.month,
                               time.day, time.hour, time.minute, time.second, 0)
            if base_time is None:
                base_time = datetime(time.year, time.month,
                                     time.day-1, 0, 0, 0, 0)
            timedelta = pd.Timedelta(newTime - base_time).total_seconds()//60
            humidityObj.append(CorellationModel(
                float(hum.humidity), int(timedelta)))

        for temp in Temperature.objects.all():
            time = temp.dateTime
            newTime = datetime(time.year, time.month,
                               time.day, time.hour, time.minute, time.second, 0)
            if base_time_temp is None:
                base_time_temp = datetime(
                    time.year, time.month, time.day-1, 0, 0, 0, 0)
            timedelta = pd.Timedelta(
                newTime - base_time_temp).total_seconds()//60
            temperatureObj.append(CorellationModel(
                float(temp.temperature), int(timedelta)))

        humList = []
        tempList = []
        dateList = []
        for te in temperatureObj:
            if te.time in dateList:
                continue
            for hum in humidityObj:
                if (te.time == hum.time):
                    humList.append(hum.value)
                    tempList.append(te.value)
                    dateList.append(te.time)
                    humidityObj.remove(hum)
                    break
        print(humList)
        print(tempList)
        print(dateList)
        return pd.DataFrame(
            {
                'date': dateList,
                'temperature': tempList,
                'humidity': humList
            }
        )
    
    def getTestDataPr(self):
        pr = self.getCorellationFramePr()
        Y = pr['pressure']
        X = pr.drop('pressure', axis=1)
        print(X)
        X_train, X_test, y_train, y_test = train_test_split(
            X, Y, test_size=0.25, random_state=143)

        lnorm_transf = LNormalizer()
        skl_pipeline = Pipeline(
            steps=[('normalizer', lnorm_transf), ('regression_estimator', LinearRegression())])
        skl_pipeline.fit(X_train.loc[:, ['date', 'humidity']].values, y_train)
        y_pred_pr = skl_pipeline.predict(
            X_test.loc[:, ['date', 'humidity']].values)
        rmse_pr = np.mean((np.round(y_pred_pr) - y_test.values)**2)**0.5
        print('Середнєквадратичне відхилення: {}'.format(rmse_pr))
        return y_pred_pr, rmse_pr

    def getCorellationFramePr(self):
        pressureObj = []
        humidityObj = []
        base_time = None
        base_time_hum = None

        for pr in Pressure.objects.all():
            time = pr.dateTime
            newTime = datetime(time.year, time.month,
                               time.day, time.hour, time.minute, time.second, 0)
            if base_time is None:
                base_time = datetime(time.year, time.month,
                                     time.day-1, 0, 0, 0, 0)
            timedelta = pd.Timedelta(newTime - base_time).total_seconds()//60
            pressureObj.append(CorellationModel(
                float(pr.pressure), int(timedelta)))

        for hum in Humidity.objects.all():
            time = hum.dateTime
            newTime = datetime(time.year, time.month,
                               time.day, time.hour, time.minute, time.second, 0)
            if base_time_hum is None:
                base_time_hum = datetime(
                    time.year, time.month, time.day-1, 0, 0, 0, 0)
            timedelta = pd.Timedelta(
                newTime - base_time_hum).total_seconds()//60
            humidityObj.append(CorellationModel(
                float(hum.humidity), int(timedelta)))

        prList = []
        humList = []
        dateList = []
        
        for hu in humidityObj:
            if hu.time in dateList:
                continue
            for pr in pressureObj:
                if (hu.time == pr.time):
                    prList.append(pr.value)
                    humList.append(hu.value)
                    dateList.append(hu.time)
                    pressureObj.remove(pr)
                    break
        print(prList)
        print(humList)
        print(dateList)
        return pd.DataFrame(
            {
                'date': dateList,
                'humidity': humList,
                'pressure': prList
            }
        )

    def dateTimeFormatter(self, date):
        return date.strftime("%m/%d/%Y, %H")

    def dateTimeFormatterMean(self, date):
        return date.strftime("%m/%d/%Y")

class CorellationModel:
    def __init__(self, value, time):
        self.value = value
        self.time = time
