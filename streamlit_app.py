#created the main python file
import pandas as pd
import streamlit
import requests
streamlit.title('Hello Usman')
streamlit.header('Monday Tasks')
streamlit.text('Learn snowflake')
fruits_read=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_index=fruits_read.set_index('Fruit')
fruits_multi=streamlit.multiselect("Select fruits:",list(fruits_index.index))
fruits=fruits_index.loc[fruits_multi]
streamlit.dataframe(fruits)
streamlit.header('Json response')
fruit_choice=streamlit.text_input("Which fruit information would you like to get ?",'')
response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
response_json = response.json()
response_normalized = pd.json_normalize(response_json)
streamlit.dataframe(response_normalized)
