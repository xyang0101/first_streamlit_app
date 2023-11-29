import streamlit

streamlit.title('My Parent New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3')
streamlit.text('Kale')
streamlit.text('Egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
