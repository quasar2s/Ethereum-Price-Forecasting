# Ethereum Price Forecasting
![eth](https://user-images.githubusercontent.com/72506158/182414873-36a01f27-f8d3-4513-8665-055cfeb91c40.png)

# Introduction
Ethereum is a technology that's home to digital money, global payments, and applications. It is the second-largest cryptocurrency by market capitalization, right behind Bitcoin. Predicting Ethereum's price is difficult, this is because of how volatile it is, especially since it’s still nascent in its development. This work involves developing a time-series forecasting model using Facebook's open source library Prophet that forecasts Ethereum's price trend for the next five years and predicts its price for any date in that period.

# Libraries 
**Prophet** : Prophet is an open source library developed by Facebook's data-science team for forecasting time series data based on an additive regression model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. At its core, the Prophet has four main components:
- A piecewise linear or logistic growth curve trend. Prophet automatically detects changes in trends by selecting changepoints from the data.
- A yearly seasonal component modeled using Fourier series.
- A weekly seasonal component using dummy variables.
- A user-provided list of important holidays.

 Prophet is robust to handling seasonal effects and missing data and shifts in the trend, and typically handles outliers well.

**PyStan** : PyStan is a Python interface to Stan, a package for Bayesian inference.
Stan® is a state-of-the-art platform for statistical modeling and high-performance statistical computation. Stan is used for statistical modeling, data analysis, and prediction 


**yfinance** : To get the data on Ethereum prices, yfinance library is used, Yahoo! Finance market data downloader.

**Pandas** : Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language. Prophet requires data to be in Pandas DataFrames.

**Holidays** : A fast, efficient Python library for generating country- and subdivision- (e.g. state or province) specific sets of government-designated holidays on the fly. It aims to make determining whether a specific date is a holiday as fast and flexible as possible.


# Hyperparameter Tuning
A considerable amount of research was done for tuning parameters:

growth: 'logistic' 

n_changepoints: Number of potential changepoints to include. 3 was selected as Ethereum is likely to get three big updates in the coming five years. First one being The Merge : It will mark the end of proof-of-work for Ethereum, and the full transition to proof-of-stake. This will reduce Ethereum's energy consumption by ~99.95%.

changepoint_range: Proportion of history in which trend changepoints will be estimated. Defaults to 0.8 for the first 80%. 1 was chosen to estimate trend changepoints from entire history. 

yearly_seasonality: 'True'

holidays: Since almost 49% of all eth is owned by US. To account holiday's effect on Ethereum, a data-frame contating list of all US holidays was inserted in model.

seasonality_mode: 'multiplicative'. It’s a multiplicative time series because of how cryptocurrency price fluctuates by the year, which also means the seasonal component changing with trend.

changepoint_prior_scale: By default, this parameter is set to 0.05. Increasing it will make the trend more flexible. 0.5 was selected considering volatile nature of crypto market as a whole. 


# Output 
**Forecast**

![result 1](https://user-images.githubusercontent.com/72506158/182445277-92473ffc-29f2-4010-9cac-336614edc91e.png)

**Components**

![result 2](https://user-images.githubusercontent.com/72506158/182445462-005335a4-28e9-468c-b9f5-ec00bd9ea445.png)






