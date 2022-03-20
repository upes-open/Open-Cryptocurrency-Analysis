import requests
import json
import pandas as pd
from datetime import date

url = "https://yfapi.net/v8/finance/spark" #url used to access historical data from the API

querystring = {"interval": "1d","range":"max","symbols": "BTC-INR,ETH-INR,ADA-INR"} #the request sent to the API. Gives data in daily intervals for the max range for the given currencies

headers = {'x-api-key': "api-key"} #your personal api key goes here

response = requests.request("GET", url, headers=headers, params=querystring) #Sends the request to the API. If successful, we get a JSON file in return

data = json.loads(response.text) #converts the JSON into easily readable python dictionary/list

btc_time = data['BTC-INR']['timestamp']
btc_time = list(map(date.fromtimestamp,btc_time))
btc_time = list(map(str,btc_time)) #Extracting the dates and converting them into human readable format

btc_rate = data['BTC-INR']['close'] #extracting the price of the currency at different times

#same process is repeated for different currencies

eth_time = data['ETH-INR']['timestamp']
eth_time = list(map(date.fromtimestamp,eth_time))
eth_time = list(map(str,eth_time))

eth_rate = data['ETH-INR']['close']

ada_time = data['ADA-INR']['timestamp']
ada_time = list(map(date.fromtimestamp,ada_time))
ada_time = list(map(str,ada_time))

ada_rate = data['ADA-INR']['close']

#Compiling the data of each currency into a DataFrame
btc = pd.DataFrame(data = [btc_time,btc_rate])
btc = btc.T
eth = pd.DataFrame(data = [eth_time,eth_rate])
eth = eth.T
ada = pd.DataFrame(data = [ada_time,ada_rate])
ada = ada.T

#Saving the DataFrame in the form of a csv file
btc.to_csv("btc_data.csv")
eth.to_csv("eth_data.csv")
ada.to_csv("ada_data.csv")
