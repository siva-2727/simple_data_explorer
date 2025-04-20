import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Simple Data Explorer")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    # Load CSV data
    df = pd.read_csv(uploaded_file)
    
    # Display dataframe
    st.write("Dataframe Preview:", df)
    
    # Select column to visualize
    column = st.selectbox("Select a column to visualize", df.columns)
    
    # Create and display a histogram
    plt.hist(df[column], bins=20)
    st.pyplot(plt)
