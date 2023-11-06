#created the main python file
import pandas as pd
import streamlit
streamlit.title('Hello Usman')
streamlit.header('Monday Tasks')
streamlit.text('Learn snowflake')
fruits=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(fruits)
