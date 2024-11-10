import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

st.set_page_config(page_title="Data Analysis Darhboard",layout="wide")

if 'previous_file' not in st.session_state:
    st.session_state.previous_file = None
    st.session_state.title = "Data Analysis Dashboard"

st.title(st.session_state.title)
st.write("Data Analysis Dashboard")

# FIle upload
uploaded = st.file_uploader("Upload your CSV file",type="csv")

if uploaded and uploaded != st.session_state.previous_file:
    st.session_state.title = f"{uploaded.name.split(".csv" or ".excel")[0]} Analysis Dashboard"
    st.session_state.previous_file = uploaded
    st.rerun()

if uploaded:
    
    @st.cache_data
    def load_data(file):
     return pd.read_csv(file)
    data = load_data(uploaded)

    # data = pd.read_csv(uploaded)
    st.sidebar.header("Dashboard Options")
    show_data_overview=st.sidebar.checkbox("Data Overview")
    show_data_cleaning=st.sidebar.checkbox("Data Cleaning Options")
    show_visualization_options=st.sidebar.checkbox("visualization options")

    if show_data_overview:
       st.header("Data Overview") 
       st.write("#### Dataset Preview")

       st.write(f"Data Shape: {data.shape[0]} rows, {data.shape[1]} columns")
       st.dataframe(data.head(10))

       selected_columns=st.multiselect("Select columns to view details",options=data.columns)
       if selected_columns:
          st.write(f"Showing selected columns: {selected_columns}")
          st.dataframe(data[selected_columns])
    if show_data_cleaning:
       st.header("Data Cleaning")
       file_missing_Values=st.selectbox("How would you like to handle missing values?" ,["None","Fill with zero"])
       if file_missing_Values== "Fill with zero":
          data.fillna(0,inplace=True)
       if st.checkbox("Remove Duplicate rows"):
          data.drop_duplicates(inplace=True)
          st.write("Duplicates Removed")
       st.write("Cleaned data Sample")
       st.dataframe(data.head(10))
    if show_visualization_options:
       st.header("Data Visualization")
       Visualization_Option=st.selectbox("How would you like to Visualize your data?" ,["Pie Chart","Bar Graph","Histogram","Heatmap"])
       if Visualization_Option=="Pie Chart":
          ...
       if Visualization_Option=="Bar Graph":
          ...
       if Visualization_Option=="Histogram":
          ...
       if Visualization_Option=="Heatmap":
          ...
       
       

else:
   st.info("Please upload your CSV File")

