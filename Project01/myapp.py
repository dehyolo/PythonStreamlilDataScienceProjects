import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Aplicativo Simples de Preços de Ações

São mostrados o preço de **fechamento** e ***volume*** das ações do Google

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
