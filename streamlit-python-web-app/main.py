"""
THIS PROJECT GOAL IS TO DEMONSTRATE THE CAPABILITY OF STREAMLIT TO BUILD AN PYTHON APPLICATION
"""
import streamlit as st
import pandas as pd
import numpy as np


time_series_covid19_confirmed_US = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
time_series_covid19_confirmed_global= 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
time_series_covid19_deaths_US = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'
time_series_covid19_deaths_global = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
time_series_covid19_recovered_global = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'


confirmed_US = pd.read_csv(time_series_covid19_confirmed_US)
confirmed_global = pd.read_csv(time_series_covid19_confirmed_global)
deaths_US = pd.read_csv(time_series_covid19_deaths_US)
deaths_global = pd.read_csv(time_series_covid19_deaths_global)
recovered_global = pd.read_csv(time_series_covid19_recovered_global)
confirmed_US.columns.tolist(), confirmed_global.columns,deaths_US.columns,deaths_global.columns,recovered_global.columns


