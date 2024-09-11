import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz
import time

# Define your custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    
    body {
        font-family: 'Roboto', sans-serif;
    }
    
    .title {
        font-size: 100px;
        text-align: center;
        font-weight: bold;
    }
    
    .countdown {
        font-size: 30px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Set up the layout
st.markdown('<p class="title">Coming Soon!</p>', unsafe_allow_html=True)

gmt_plus_7 = pytz.timezone('Asia/Bangkok')

next_friday = datetime(2024, 9, 20, tzinfo=gmt_plus_7)

clock_placeholder_date = st.empty()
test_placeholder = st.empty()

def calculate_elapsed_time(start_date):
    now = datetime.now(gmt_plus_7)
    delta = relativedelta(start_date, now)
    return delta.days


variable_date = True

while variable_date:
    now = datetime.now(gmt_plus_7)
    days = calculate_elapsed_time(next_friday)
    clock_placeholder_date.markdown(f'<p class="countdown">{days} days remaining</p>', unsafe_allow_html=True)
    time.sleep(1)

    if now >= next_friday:
        variable_date = False



