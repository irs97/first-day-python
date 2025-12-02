import streamlit as st
import random

st.title("🎯 Simple Guessing Game")

# Initialize the secret number in session state
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.message = "I picked a number between 1 and 100. Try to guess!"

st.write(st.session_state.message)

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    if guess == st.session_state.secret:
        st.session_state.message = f"🎉 Correct! The number was {st.session_state.secret}. Starting a new game..."
        st.session_state.secret = random.randint(1, 100)
    elif guess < st.session_state.secret:
        st.session_state.message = "🔼 Too low! Try again."
    else:
        st.session_state.message = "🔽 Too high! Try again."

    st.experimental_rerun()
