#importing neccessary libraries
from turtle import width
import yfinance as yf
import streamlit as st
from PIL  import Image
from urllib.request import urlopen
from datetime import date

today = date.today()


#Titles and Headings
st.set_page_config(page_title='Crypto-Analysis', layout = "centered")
st.title("Cryptocurrency Analysis - OPEN")
st.header("Dashboard")
st.markdown(""" <style>
</style> """, unsafe_allow_html=True)


#Defining ticker variables
Bitcoin = 'BTC-INR'
Ethereum = 'ETH-INR'
Ripple = 'XRP-INR'
BitcoinCash = 'BCH-INR'


# Data accessing from Yahoo Finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)


#Data Fetching from Yahoo Finance
BTC_His = BTC_Data.history(period = 'max')
ETH_His = ETH_Data.history(period = 'max')
XRP_His = XRP_Data.history(period = 'max')
BCH_His = BCH_Data.history(period = 'max')


#Fetching Crypto Data from Data Frame
BTC = yf.download(Bitcoin, start=today, end=today)
ETH = yf.download(Ethereum, start=today, end=today)
XRP = yf.download(Ripple, start=today, end=today)
BCH = yf.download(BitcoinCash, start=today, end=today)

#Bitcoin
st.subheader("Bitcoin (INR)")
imageBTC = Image.open(urlopen('https://pngimg.com/uploads/bitcoin/bitcoin_PNG48.png'))

#Display Image
st.image(imageBTC, width = 240)

#Display Dataframe
st.table(BTC)

#Display a Chart
st.area_chart(BTC_His.Close)
st.markdown("***")



#Ethereum
st.subheader("Ethereum (INR)")
imageETH = Image.open(urlopen('https://www.pngall.com/wp-content/uploads/10/Ethereum-Logo-PNG.png'))

#Display Image
st.image(imageETH, width = 240)

#Display Dataframe
st.table(ETH)

#Display a Chart
st.area_chart(ETH_His.Close)
st.markdown("***")



#Ripple
st.subheader("Ripple (INR)")
imageXRP = Image.open(urlopen('https://ripple.com/wp-content/uploads/2020/07/ripple-triskelion-512.png'))

#Display Image
st.image(imageXRP, width = 240)

#Display Dataframe
st.table(XRP)

#Display a Chart
st.area_chart(XRP_His.Close)
st.markdown("***")



#BitcoinCash
st.subheader("BitcoinCash (INR)")
imageBCH = Image.open(urlopen('https://upload.wikimedia.org/wikipedia/commons/5/58/Bitcoin_Cash.png'))

#Display Image
st.image(imageBCH, width = 240)

#Display Dataframe
st.table(BCH)

#Display a Chart
st.area_chart(BCH_His.Close)

