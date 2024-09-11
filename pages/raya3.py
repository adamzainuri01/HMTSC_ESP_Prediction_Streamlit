import streamlit as st
import os
from math import ceil
from PIL import Image

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    
    body {
        font-family: 'Roboto', sans-serif;
    }
    
    .title {
        font-size: 50px;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Define the directory containing images
image_dir = './images/album3'

# Get list of image files
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Count the number of image files
N = len(image_files)

# Calculate the number of rows needed
rows = ceil(N / 3)

# Display images in a grid layout
st.markdown('<p class="title">My Beautiful</p>', unsafe_allow_html=True)

# Loop through rows
for i in range(rows):
    # Create 3 columns in the current row
    cols = st.columns(3)

    # Loop through columns
    for j in range(3):
        # Calculate the index of the image to display
        index = i * 3 + j

        if index < N:
            # Open and display the image
            image_path = os.path.join(image_dir, image_files[index])
            image = Image.open(image_path)
            cols[j].image(image, use_column_width=True)
        else:
            # Empty column if there are fewer images than columns
            cols[j].empty()
