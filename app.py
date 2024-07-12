import streamlit as st
import requests
import time
from datetime import datetime

# Function to get crypto price from a public API
def get_crypto_price(crypto='bitcoin'):
    url = f'https://api.coindesk.com/v1/bpi/currentprice/{crypto}.json'
    response = requests.get(url)
    data = response.json()
    return data['bpi']['USD']['rate_float']

# Initializing the game state
if 'previous_price' not in st.session_state:
    st.session_state.previous_price = get_crypto_price()
    st.session_state.score = 0

# Title
st.title("Crypto Price Prediction Game")

# Instructions
st.write("""
    Guess if the price of Bitcoin will go up or down in the next minute.
    Click the button below to submit your guess.
""")

# Buttons for user guess
col1, col2 = st.columns(2)
with col1:
    if st.button('Price will go UP'):
        st.session_state.guess = 'up'
with col2:
    if st.button('Price will go DOWN'):
        st.session_state.guess = 'down'

# Wait for a minute and get the new price
time.sleep(60)
current_price = get_crypto_price()

# Determine if the user's guess was correct
if 'guess' in st.session_state:
    if (st.session_state.guess == 'up' and current_price > st.session_state.previous_price) or \
       (st.session_state.guess == 'down' and current_price < st.session_state.previous_price):
        st.session_state.score += 1
        st.success("Correct guess!")
    else:
        st.error("Wrong guess!")
    
    st.write(f"Previous Price: ${st.session_state.previous_price:.2f}")
    st.write(f"Current Price: ${current_price:.2f}")
    st.write(f"Your Score: {st.session_state.score}")

# Update previous price for the next round
st.session_state.previous_price = current_price

# Refresh button to play again
if st.button('Play Again'):
    st.experimental_rerun()

