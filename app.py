import streamlit as st
import requests
import time

# Function to get crypto price from a public API
def get_crypto_price(crypto='BTC'):
    url = f'https://api.coindesk.com/v1/bpi/currentprice/{crypto}.json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

# Initialize the game state
if 'previous_price' not in st.session_state:
    initial_price = get_crypto_price()
    if initial_price is not None:
        st.session_state.previous_price = initial_price
    else:
        st.session_state.previous_price = 0
    st.session_state.score = 0
    st.session_state.guess = None

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
if st.session_state.guess:
    st.write("Waiting for 60 seconds to fetch the new price...")
    time.sleep(60)
    current_price = get_crypto_price()

    if current_price is not None:
        # Determine if the user's guess was correct
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

    # Reset guess
    st.session_state.guess = None

# Refresh button to play again
if st.button('Play Again'):
    st.experimental_rerun()

