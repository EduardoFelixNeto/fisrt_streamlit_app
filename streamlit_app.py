import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu 🍞')
streamlit.text('🐔 Eggs and Bacon')
streamlit.text('🥑 Banana, Grapes, Apples and Honey')
streamlit.text('🥗 Oatmeal and Milk')  
streamlit.header('Build your own fruit smoothie')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
