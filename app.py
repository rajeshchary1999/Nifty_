import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

nifty_50 = yf.download('^NSEI', start = '2020-10-01',
                       end = '2022-11-01',
                       progress = False)

#print(nifty_50)   

def get_ticker(name):
    company = yf.Ticker(name)
    return company

company1 = get_ticker("NSEI")

nifty  = yf.download("NSEI", start="2020-10-01", end="2022-08-01")
st.write("""
### NIFTY_50
""")
st.write(company1.info['longBusinessSummary'])        
print(st.title('Nifty_50 Stocks Index'))

#st.write(nifty)

#st.line_chart(data1.values)
#st.header("Data understanding")
