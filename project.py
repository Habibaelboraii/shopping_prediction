import streamlit as st
import pandas as pd

st.title("Test App")

df = pd.read_csv("online_shoppers_intention.csv")
st.write(df.head())
