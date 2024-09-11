from datetime import datetime
import pytz
import time
from dateutil.relativedelta import relativedelta
import streamlit as st


def calculate_elapsed_time(start_date):
    now = datetime.now(gmt_plus_7)
    delta = relativedelta(now, start_date)
    return delta.years, delta.months, delta.days


# Set the timezone for GMT+7
gmt_plus_7 = pytz.timezone('Asia/Bangkok')

start_date = datetime(2022, 10, 6, tzinfo=gmt_plus_7)

# Add custom CSS for styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap');
    
    .clock-container {
        text-align: center;
        font-family: 'Roboto', sans-serif;
        margin: 0;
        padding: 0;
    }
    
    .clock-date {
        font-size: 25px;
    }
    
    .clock-time {
        font-size: 150px;
        font-weight: bold;
    }
    
    
    </style>
    """, unsafe_allow_html=True)

# Placeholders for the date and time
clock_placeholder_date = st.empty()
clock_placeholder_time = st.empty()
clock_placeholder_image = st.empty()
elapsed_time_placeholder = st.empty()

while True:
    # Get the current date and time in GMT+7
    current_date = datetime.now(gmt_plus_7).strftime('%A, %d %B %Y')
    current_time = datetime.now(gmt_plus_7).strftime('%H:%M:%S')

    years, months, days = calculate_elapsed_time(start_date)

    # Render the date and time with custom styling in HTML
    clock_placeholder_date.markdown(f"""
        <div class="clock-container">
            <div class="clock-date">{current_date}</div>
        </div>
        """, unsafe_allow_html=True)

    clock_placeholder_time.markdown(f"""
        <div class="clock-container">
            <div class="clock-time">{current_time}</div>
        </div>
        """, unsafe_allow_html=True)

    left_co, center_co, right_co = clock_placeholder_image.columns(3)
    with left_co:
        st.image("./images/image-home-2.jpg", use_column_width=True)
    with center_co:
        st.image("./images/image-home.jpg", use_column_width=True)
    with right_co:
        st.image("./images/image-home-3.jpg", use_column_width=True)

    elapsed_time_placeholder.markdown(f"""
        <div class="clock-container">
            <div class="elapsed-time">
                {years} years, {months} months, and {days} days since October 6, 2020, our first date of dating
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Update every second
    time.sleep(1)
