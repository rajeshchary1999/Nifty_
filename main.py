import pandas as pd
import numpy as np
import yfinance as yf
import streamlit as st


df = pd.read_csv("Nifty_50.csv")
st.title("Nifty 50 Stocks")


d = st.date_input("Enter simultation date")
st.write('The simultation date is ', d)

e = st.date_input("Enter end date")
st.write('The end date is ',e)

number = st.number_input('Enter your n_days_measure_perf ')
st.write('The number is',number)

eq = st.number_input('equity amount')
st.write('The equity amount',eq)



st.button('predict')
