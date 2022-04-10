#importing neccessary libraries
from turtle import width
import yfinance as yf
import streamlit as st
from PIL  import Image
from urllib.request import urlopen
from datetime import date
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
st.set_page_config(page_title='Crypto-Analysis', layout = "centered")

def main():
    page = st.sidebar.selectbox(
        "Crypto-Market",
        [
            "Cryptocurrency Prices",
            "Analysis and Visualization"
        ]
    )

    if page == "Cryptocurrency Prices":
        homepage()
    elif page == "Analysis and Visualization":
        visualz()
today = date.today()
week_ago = today - dt.timedelta(days=7)

def homepage():

    #Titles and Headings?
    st.title("Cryptocurrency Analysis - OPEN")
    st.header("Dashboard")
    st.markdown(""" <style>
    </style> """, unsafe_allow_html=True)


    #Defining ticker variables
    Bitcoin = 'BTC-INR'
    Ethereum = 'ETH-INR'
    Ripple = 'XRP-INR'
    BitcoinCash = 'BCH-INR'
    Cardano = 'ADA-INR'

    # Data accessing from Yahoo Finance
    BTC_Data = yf.Ticker(Bitcoin)
    ETH_Data = yf.Ticker(Ethereum)
    XRP_Data = yf.Ticker(Ripple)
    BCH_Data = yf.Ticker(BitcoinCash)
    ADA_Data = yf.Ticker(Cardano)

    #Data Fetching from Yahoo Finance
    BTC_His = BTC_Data.history(period = 'max')
    ETH_His = ETH_Data.history(period = 'max')
    XRP_His = XRP_Data.history(period = 'max')
    BCH_His = BCH_Data.history(period = 'max')
    ADA_His = ADA_Data.history(period = 'max')

    #Fetching Crypto Data from Data Frame
    BTC = yf.download(Bitcoin, start=week_ago, end=today)
    ETH = yf.download(Ethereum, start=week_ago, end=today)
    XRP = yf.download(Ripple, start=week_ago, end=today)
    BCH = yf.download(BitcoinCash, start=week_ago, end=today)
    ADA = yf.download(Cardano, start = week_ago, end=today)
    BTC_Close = BTC['Close']
    ETH_Close = ETH['Close']
    XRP_Close = XRP['Close']
    BCH_Close = BCH['Close']
    ADA_Close = ADA['Close']

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

    #Cardano
    st.subheader("Cardano (INR)")
    imageADA = Image.open(urlopen('https://cdn4.iconfinder.com/data/icons/crypto-currency-and-coin-2/256/cardano_ada-512.png'))

    #Display Image
    st.image(imageADA, width = 240)

    #Display Dataframe
    st.table(ADA)

    #Display a Chart
    st.area_chart(ADA_His.Close)
    st.markdown("***")

def visualz():
    Bitcoin = 'BTC-INR'
    Ethereum = 'ETH-INR'
    Ripple = 'XRP-INR'
    BitcoinCash = 'BCH-INR'
    Cardano = 'ADA-INR'

    BTC_Data = yf.Ticker(Bitcoin)
    ETH_Data = yf.Ticker(Ethereum)
    XRP_Data = yf.Ticker(Ripple)
    BCH_Data = yf.Ticker(BitcoinCash)
    ADA_Data = yf.Ticker(Cardano)

    #Data Fetching from Yahoo Finance
    BTC_His = BTC_Data.history(period = 'max')
    ETH_His = ETH_Data.history(period = 'max')
    XRP_His = XRP_Data.history(period = 'max')
    BCH_His = BCH_Data.history(period = 'max')
    ADA_His = ADA_Data.history(period = 'max')

    #Fetching Crypto Data from Data Frame
    BTC = yf.download(Bitcoin, start=week_ago, end=today)
    ETH = yf.download(Ethereum, start=week_ago, end=today)
    XRP = yf.download(Ripple, start=week_ago, end=today)
    BCH = yf.download(BitcoinCash, start=week_ago, end=today)
    ADA = yf.download(Cardano, start = week_ago, end=today)
    BTC_Close = BTC['Close']
    ETH_Close = ETH['Close']
    XRP_Close = XRP['Close']
    BCH_Close = BCH['Close']
    ADA_Close = ADA['Close']


    st.subheader("Below are the Visualizations performed by OPEN Team:   ")
    st.header(" ")
    image1 = Image.open(urlopen('https://www.kaggleusercontent.com/kf/92523879/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..2ykaHKRRhCM6QVYrp3aUnA.gPWGGA7jj0L9QYeH6MSQuwAsbOaa_UUfNMhlaEcEEwoNVBjqU2f1VNuE2C5ieadbXtnZTWe06pUxXchQntQz3Jt7q8HJTBg0bb7UYJsLfBGvuN2yWI3dB06UPaY1nd_ZfN6rGZVzfQVdiAKTV4wCWbxBkgVRctVAxf4EUkLStNa7uK3tvlxrJLPOc6wZ2fbBgGW21ezc4PqOKZo7K0VpB3UFvRHCFcAXlCcoOPPvhcLhHElPf-VAO9DYjAkOgjnN55Mp-_wje9skxAV9txCOlhI8BrmRxbtMMDIYq8eW4u-OZ3kt4IotiO4xBLBt-6DyYRKtNSuZ-IunDJjsblx1Es5gSjwx44eqO9VUfwcICEGNQluZtIhg4gRTYda_y0uLY0mr7YCeznSXVh_RBcrWLUKOfSjWOVti4rGVq5j0ngoAXQiEapGPEwSDrhowb-ap6VjG3Pypkp6hGH1sQHQOmDS1sV4wlXoCFJYuRxg9oeoVl-6YGmswKK_a4eXuokqLTy1GWjRa0tbotOIHgUK8eETxP7l9V070oK72LKbEcD9M9wqpvz3Bk6FFkvJGNfohVh9nGvSDC8c4hnEoQ0GSRqka6razN7sw--MnOGFTDsVB_uCo78Oxb3QGsWj5LrFqZcl5eh64B4GT_nWtaZM-cQ.u9zYDivALhXdmDSRFIkv5Q/__results___files/__results___45_0.png'))
    #st.image(image1)
    image2 = Image.open(urlopen('https://www.kaggleusercontent.com/kf/92523879/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..2ykaHKRRhCM6QVYrp3aUnA.gPWGGA7jj0L9QYeH6MSQuwAsbOaa_UUfNMhlaEcEEwoNVBjqU2f1VNuE2C5ieadbXtnZTWe06pUxXchQntQz3Jt7q8HJTBg0bb7UYJsLfBGvuN2yWI3dB06UPaY1nd_ZfN6rGZVzfQVdiAKTV4wCWbxBkgVRctVAxf4EUkLStNa7uK3tvlxrJLPOc6wZ2fbBgGW21ezc4PqOKZo7K0VpB3UFvRHCFcAXlCcoOPPvhcLhHElPf-VAO9DYjAkOgjnN55Mp-_wje9skxAV9txCOlhI8BrmRxbtMMDIYq8eW4u-OZ3kt4IotiO4xBLBt-6DyYRKtNSuZ-IunDJjsblx1Es5gSjwx44eqO9VUfwcICEGNQluZtIhg4gRTYda_y0uLY0mr7YCeznSXVh_RBcrWLUKOfSjWOVti4rGVq5j0ngoAXQiEapGPEwSDrhowb-ap6VjG3Pypkp6hGH1sQHQOmDS1sV4wlXoCFJYuRxg9oeoVl-6YGmswKK_a4eXuokqLTy1GWjRa0tbotOIHgUK8eETxP7l9V070oK72LKbEcD9M9wqpvz3Bk6FFkvJGNfohVh9nGvSDC8c4hnEoQ0GSRqka6razN7sw--MnOGFTDsVB_uCo78Oxb3QGsWj5LrFqZcl5eh64B4GT_nWtaZM-cQ.u9zYDivALhXdmDSRFIkv5Q/__results___files/__results___45_1.png'))       
    
    image3 = Image.open(urlopen('https://www.kaggleusercontent.com/kf/92523879/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..2ykaHKRRhCM6QVYrp3aUnA.gPWGGA7jj0L9QYeH6MSQuwAsbOaa_UUfNMhlaEcEEwoNVBjqU2f1VNuE2C5ieadbXtnZTWe06pUxXchQntQz3Jt7q8HJTBg0bb7UYJsLfBGvuN2yWI3dB06UPaY1nd_ZfN6rGZVzfQVdiAKTV4wCWbxBkgVRctVAxf4EUkLStNa7uK3tvlxrJLPOc6wZ2fbBgGW21ezc4PqOKZo7K0VpB3UFvRHCFcAXlCcoOPPvhcLhHElPf-VAO9DYjAkOgjnN55Mp-_wje9skxAV9txCOlhI8BrmRxbtMMDIYq8eW4u-OZ3kt4IotiO4xBLBt-6DyYRKtNSuZ-IunDJjsblx1Es5gSjwx44eqO9VUfwcICEGNQluZtIhg4gRTYda_y0uLY0mr7YCeznSXVh_RBcrWLUKOfSjWOVti4rGVq5j0ngoAXQiEapGPEwSDrhowb-ap6VjG3Pypkp6hGH1sQHQOmDS1sV4wlXoCFJYuRxg9oeoVl-6YGmswKK_a4eXuokqLTy1GWjRa0tbotOIHgUK8eETxP7l9V070oK72LKbEcD9M9wqpvz3Bk6FFkvJGNfohVh9nGvSDC8c4hnEoQ0GSRqka6razN7sw--MnOGFTDsVB_uCo78Oxb3QGsWj5LrFqZcl5eh64B4GT_nWtaZM-cQ.u9zYDivALhXdmDSRFIkv5Q/__results___files/__results___45_2.png'))       
    st.image([image1, image2, image3])
    st.header(" ")
    image4 = Image.open(urlopen('https://www.kaggleusercontent.com/kf/92523879/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..2ykaHKRRhCM6QVYrp3aUnA.gPWGGA7jj0L9QYeH6MSQuwAsbOaa_UUfNMhlaEcEEwoNVBjqU2f1VNuE2C5ieadbXtnZTWe06pUxXchQntQz3Jt7q8HJTBg0bb7UYJsLfBGvuN2yWI3dB06UPaY1nd_ZfN6rGZVzfQVdiAKTV4wCWbxBkgVRctVAxf4EUkLStNa7uK3tvlxrJLPOc6wZ2fbBgGW21ezc4PqOKZo7K0VpB3UFvRHCFcAXlCcoOPPvhcLhHElPf-VAO9DYjAkOgjnN55Mp-_wje9skxAV9txCOlhI8BrmRxbtMMDIYq8eW4u-OZ3kt4IotiO4xBLBt-6DyYRKtNSuZ-IunDJjsblx1Es5gSjwx44eqO9VUfwcICEGNQluZtIhg4gRTYda_y0uLY0mr7YCeznSXVh_RBcrWLUKOfSjWOVti4rGVq5j0ngoAXQiEapGPEwSDrhowb-ap6VjG3Pypkp6hGH1sQHQOmDS1sV4wlXoCFJYuRxg9oeoVl-6YGmswKK_a4eXuokqLTy1GWjRa0tbotOIHgUK8eETxP7l9V070oK72LKbEcD9M9wqpvz3Bk6FFkvJGNfohVh9nGvSDC8c4hnEoQ0GSRqka6razN7sw--MnOGFTDsVB_uCo78Oxb3QGsWj5LrFqZcl5eh64B4GT_nWtaZM-cQ.u9zYDivALhXdmDSRFIkv5Q/__results___files/__results___46_1.png'))       
    st.image(image4)
    image5 = Image.open(urlopen('https://www.kaggleusercontent.com/kf/92601969/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..otFcYKskBPJhArbsLwrGeQ.szuTEDSCsmN8W5FfLlSNv4Ljc7PK7eacp8Rh7L2HrcpY07L0zFtTPTzNeC1EEVP19z8N71ndA3hDMAP3kzSYyOr2JjD13Wb1jYHq6ouBizxVPyUSTb_iAW7eyH7JqMjl3NY1t8IZJb9524VyrxKb8srQNM-d1URLFdtvGwNHP28Ly66xd4bvJAuZ0o2dvtduDomch1IhV1kjSJDEB1joNUwxK0EUBMK2Ynll3BPzhFJ2kYaN64x5S8r7KepNg7F0zGa6lo7jVPXkW5ksmhwq41crBwikuLImIhtjdu0RsCKVoy0E4YGlGflY7K2f1bNRbFu0jppGtm9ocAk6Rmz_f_jZ7qQxxNnkJPfphtBc4K8O6Vvpx-T8W9I6518sXeJEF1IJbmc55DG4qbCRy1VaTbHIbqsy_OA0rUkXl23fYxH6ZsEa72o0cbShEz1WWK-92ZRD-F_eVJIKic4JV60c4EYzB_1Jk3r-bjCdSBFmmTyvGMVsG-DSfHQHfmivSbAq3yCxpCxflmkMkcZq8u16FJoY6rXiwUgFKIa_Wzdy30nFa3ZrLm8ihHhnRuUwu-YvqPr6j5m4P7fuT_iuxBBADRFyQYl7M6SGNbpqicOfZeshxM40G0o5qAu_BqQAQQrdbRnaUZFBE-JNe6Jc3yrnm6Xs6T2mo_nfBn3jtPCzWMKWejfVnpxm8SpB_ASrq2Kf.rxVFw0WbvZDzoWiZGN8s3g/__results___files/__results___31_0.png'))
    st.image(image5)

    image6 = Image.open(urlopen('https://www.kaggleusercontent.com/kf/92601969/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..otFcYKskBPJhArbsLwrGeQ.szuTEDSCsmN8W5FfLlSNv4Ljc7PK7eacp8Rh7L2HrcpY07L0zFtTPTzNeC1EEVP19z8N71ndA3hDMAP3kzSYyOr2JjD13Wb1jYHq6ouBizxVPyUSTb_iAW7eyH7JqMjl3NY1t8IZJb9524VyrxKb8srQNM-d1URLFdtvGwNHP28Ly66xd4bvJAuZ0o2dvtduDomch1IhV1kjSJDEB1joNUwxK0EUBMK2Ynll3BPzhFJ2kYaN64x5S8r7KepNg7F0zGa6lo7jVPXkW5ksmhwq41crBwikuLImIhtjdu0RsCKVoy0E4YGlGflY7K2f1bNRbFu0jppGtm9ocAk6Rmz_f_jZ7qQxxNnkJPfphtBc4K8O6Vvpx-T8W9I6518sXeJEF1IJbmc55DG4qbCRy1VaTbHIbqsy_OA0rUkXl23fYxH6ZsEa72o0cbShEz1WWK-92ZRD-F_eVJIKic4JV60c4EYzB_1Jk3r-bjCdSBFmmTyvGMVsG-DSfHQHfmivSbAq3yCxpCxflmkMkcZq8u16FJoY6rXiwUgFKIa_Wzdy30nFa3ZrLm8ihHhnRuUwu-YvqPr6j5m4P7fuT_iuxBBADRFyQYl7M6SGNbpqicOfZeshxM40G0o5qAu_BqQAQQrdbRnaUZFBE-JNe6Jc3yrnm6Xs6T2mo_nfBn3jtPCzWMKWejfVnpxm8SpB_ASrq2Kf.rxVFw0WbvZDzoWiZGN8s3g/__results___files/__results___44_0.png'))
    st.image(image6)
    image7 = Image.open(urlopen('https://www.kaggleusercontent.com/kf/92601969/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..otFcYKskBPJhArbsLwrGeQ.szuTEDSCsmN8W5FfLlSNv4Ljc7PK7eacp8Rh7L2HrcpY07L0zFtTPTzNeC1EEVP19z8N71ndA3hDMAP3kzSYyOr2JjD13Wb1jYHq6ouBizxVPyUSTb_iAW7eyH7JqMjl3NY1t8IZJb9524VyrxKb8srQNM-d1URLFdtvGwNHP28Ly66xd4bvJAuZ0o2dvtduDomch1IhV1kjSJDEB1joNUwxK0EUBMK2Ynll3BPzhFJ2kYaN64x5S8r7KepNg7F0zGa6lo7jVPXkW5ksmhwq41crBwikuLImIhtjdu0RsCKVoy0E4YGlGflY7K2f1bNRbFu0jppGtm9ocAk6Rmz_f_jZ7qQxxNnkJPfphtBc4K8O6Vvpx-T8W9I6518sXeJEF1IJbmc55DG4qbCRy1VaTbHIbqsy_OA0rUkXl23fYxH6ZsEa72o0cbShEz1WWK-92ZRD-F_eVJIKic4JV60c4EYzB_1Jk3r-bjCdSBFmmTyvGMVsG-DSfHQHfmivSbAq3yCxpCxflmkMkcZq8u16FJoY6rXiwUgFKIa_Wzdy30nFa3ZrLm8ihHhnRuUwu-YvqPr6j5m4P7fuT_iuxBBADRFyQYl7M6SGNbpqicOfZeshxM40G0o5qAu_BqQAQQrdbRnaUZFBE-JNe6Jc3yrnm6Xs6T2mo_nfBn3jtPCzWMKWejfVnpxm8SpB_ASrq2Kf.rxVFw0WbvZDzoWiZGN8s3g/__results___files/__results___66_0.png'))
    st.image(image7)

if __name__ == "__main__":
    main()
