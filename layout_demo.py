import streamlit as st
import numpy as np


st.title("Layout Demo")

# Sidebar
st.header("Sidebar Elements")
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0, 100, (10,50)
)

#st.write(f"Contact method: {add_selectbox}")
#st.write(f"Selected range: {add_slider}")
st.write('Selected Contact method -',add_selectbox)
st.write('Selected Range' \
'',add_slider)

# Columns
st.header("Columns Layout")
left_column, right_column = st.columns(2)

# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting City',
        ("Vadodara", "Anand", "Ahmedabad", "Surat")
    )
    st.write(f"You are in {chosen} City!")

    ### Another Column Layout

    c1, c2 = st.columns(2)
    select_box = c1.selectbox('',('English','Gujarati','Hindi'))
    email_id = c2.text_input('Email ID')