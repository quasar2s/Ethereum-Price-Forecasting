# -*- coding: utf-8 -*-
"""Eth_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HdK9izqx-6u7BdfCrxGDWn-w4OrzeL_I

INSTALLING LIBRARIES
"""

!pip install pystan==2.19.1.1
!pip install fbprophet
!pip install yfinance
!pip install holidays

"""LOADING LIBRARIES"""

import pandas as pd
import yfinance as yf
from datetime import datetime
from datetime import date
import holidays
from datetime import timedelta
import plotly.graph_objects as go
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, plot_components_plotly
import warnings
warnings.filterwarnings('ignore')
pd.options.display.float_format = '${:,.2f}'.format

"""GETTING THE DATA"""

today = datetime.today().strftime('%Y-%m-%d')
start_date = '2018-01-01'
eth_df = yf.download('ETH-USD', start_date, today)
eth_df.head()

"""EDA"""

eth_df.describe()

eth_df.info()

eth_df.columns

eth_df.reset_index(inplace = True)
eth_df.columns

eth_df.head()

df = eth_df[['Date', 'Open']]
new_names = {'Date':'ds', 'Open':'y'}
df.rename(columns = new_names, inplace = True)
df['cap'] = 50000

df.tail()

"""Accounting Holidays effect on Ethereum"""

#defining dynamic end date as 5 years from "today"
end_date = ""
count = 0
for ele in today:
  if count == 3:
    ele = str(int(ele) + 5)
  end_date += ele
  count += 1

end_year = int(end_date[0:4]) + 1


#Giving value to each date
def val(string):
  year_value = int(string[0:4])
  month_value = int(string[5:7])
  date_value = int(string[8:])
  return [year_value, month_value, date_value]

end_year_value = val(end_date)
  

HolidayList = []
for yrs in range(2018,end_year):
  for ptr in holidays.UnitedStates(years = yrs).items():
    HolidayList.append(ptr)

countt = 0
for ele in reversed(HolidayList):

  year = val(str(ele[0]))[0]
  month = val(str(ele[0]))[1]
  day = val(str(ele[0]))[2] 

  if year <= end_year_value[0]:
    if month <= end_year_value[1]:
      if day <= end_year_value[2]:
        break
  countt += 1



HolidayList = HolidayList[0:-countt]
df_holiday = pd.DataFrame(HolidayList)
df_holiday.reset_index(inplace = True)
df_holiday = df_holiday[[0,1]]
new_names = {0:'ds', 1: 'holiday'}
df_holiday.rename(columns = new_names, inplace = True)
df_holiday.head()

# plot the open price
x = df["ds"]
y = df["y"]
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y))

# Set title
fig.update_layout(
    title_text="Time series plot of Ethereum Open Price",
)

fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all"),
                ]
            )
        ),
        rangeslider=dict(visible=True),
        type="date",
    )
)

"""Prophet Model"""

m = Prophet(growth = 'logistic', n_changepoints = 3, changepoint_range = 1, yearly_seasonality = True,
            seasonality_mode = "multiplicative", changepoint_prior_scale=0.5, holidays = df_holiday)
m.fit(df)

future = m.make_future_dataframe(periods = 1827)
future['cap'] = 50000
future.tail()

forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

"""CHECK PREDICTION FOR ANY DAY WITHIN NEXT 5 YEAR"""

date = (datetime(2022,11,23) + timedelta(days=1)).strftime('%Y-%m-%d')

forecast[forecast['ds'] == date]['yhat'].item()

plot_plotly(m, forecast)

plot_components_plotly(m, forecast)