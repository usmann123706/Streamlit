import pandas as pd
import streamlit
import requests
import snowflake.connector
from urllib.error import URLError
def get_fruityvice_Date(fruit_choice):
  response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  response_json = response.json()
  return response_json
streamlit.title('Hello Usman')
streamlit.header('Monday Tasks')
streamlit.text('Learn snowflake')
fruits_read=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_index=fruits_read.set_index('Fruit')
fruits_multi=streamlit.multiselect("Select fruits:",list(fruits_index.index))
fruits=fruits_index.loc[fruits_multi]
streamlit.dataframe(fruits)
streamlit.header('Json response')
try: 
  fruit_choice=streamlit.text_input("Which fruit information would you like to get ?")
  if not fruit_choice:
    streamlit.error("please enter fruit to get information")
  else:
    back_from_function= get_fruityvice_Date(fruit_choice)
    response_normalized = pd.json_normalize(back_from_function)
    streamlit.dataframe(response_normalized)
except URLError as e:
  streamlit.error()
if streamlit.button("get fruit list"):
  my_connector=snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_cursor=my_connector.cursor()
  my_cursor.execute("select * from FRUIT_LOAD_LIST")
  my_cursor_rows=my_cursor.fetchall()
  streamlit.header("Fruit list contains")
  streamlit.dataframe(my_cursor_rows)
fruit_add=streamlit.text_input("What fruit woudl you like to add ?",'orange')
