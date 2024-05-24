# Streamlit Hierarchical Multivariate Time Series Classification for ESP Failure
A streamlit script for a web-based application to facilitate the use of predicting ESP failure information

## General Information
A simple [streamlit](https://streamlit.io) app to predict information regarding ESP Failure. This application has the following feature:  
a. Accepts multiple well inputs, either in the same Excel file or different Excel file.  
b. Shows different types of graphs, including the original sensors, derivatives of the sensors, rolling means of the sensors, and directions of the sensors.  
c. All graphs and charts are interactive.  
d. Shows statistics of the most likely prediction and least likely predictions.

## Live App
To view the application, simply go to this website [here](https://hmtsc-esp-failure-prediction.streamlit.app/). This application is hosted by [streamlit](https://streamlit.io).

## Installing the App Locally
### Install the required modules
```
pip install streamlit
pip install plotly
pip install numpy
pip install pandas
pip install pickle
```
### Running the App
```
streamlit run https://raw.githubusercontent.com/adamzainuri01/HMTSC_ESP_Prediction_Streamlit/HMTSC_Streamlit.py
```

## Required Module
- streamlit
- pandas
- numpy
- plotly
- pickle
