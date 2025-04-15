import streamlit as st
import pandas as pd
import yfinance as yf


st.write("Controlla l'andamento dei tuoi titoli finanziari.")

d = {"Apple":"AAPL", "Microsoft":"MSFT", "Alphabet": "GOOG", "Tesla":"TSLA"}

title = st.selectbox("Seleziona un titolo", ["Alphabet", "Apple", "Tesla", "Microsoft"])

st.write('Hai selezionato il ticker --> ', d[title])


t = yf.Ticker(d[title])
data = t.history(period = "5Y")


st.line_chart(data['Close'])

st.write("Visualizzazione media mobile")

numero = st.select_slider(
    "Scegli la media mobile piu' adatta alle tue esigenze",
    options=[
        0,
        7,
        14,
        21,
        28,
        35,
        42
    ],
)

st.line_chart(data['Close'].rolling(numero).mean())


st.write("calcolo e visualizzazione cambiamento percentuale")

st.line_chart(data['Close'].pct_change())










