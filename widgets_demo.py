import streamlit as st
import numpy as np
import pandas as pd

st.title("Widgets Demo")

# Slider
st.header("Slider Widget")
x = st.slider('Select a value for x', min_value=0, max_value=100, value=25)
st.write(f'{x} squared is {x * x}')

# Text Input with key
st.header("Text Input with Session State")
st.text_input("Your name", key="name")
if st.session_state.name:
    st.write(f"Hello, {st.session_state.name}!")

# Checkbox to show/hide data
st.header("Checkbox to Show/Hide Data")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.dataframe(chart_data)

# Selectbox
st.header("Selectbox")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)
st.write(f'You selected: {option}')

# Additional widgets
st.header("More Widgets")

# Radio buttons
radio_choice = st.radio(
    "Choose your favorite color:",
    ("Red", "Green", "Blue")
)
st.write(f"You chose: {radio_choice}")

# Multiselect
multiselect_options = st.multiselect(
    "Choose multiple options:",
    ["Option 1", "Option 2", "Option 3", "Option 4"],
    default=["Option 1"]
)
st.write(f"You selected: {multiselect_options}")

# Number input
number = st.number_input("Enter a number:", min_value=0, max_value=100, value=10)
st.write(f"Your number: {number}")

# Date input
import datetime
date = st.date_input("Pick a date:", datetime.date.today())
st.write(f"Selected date: {date}")

# Button
if st.button("Click me!"):
    st.write("Button was clicked!")
    st.balloons()