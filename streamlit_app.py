import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu 🍞')
streamlit.text('🐔 Eggs and Bacon')
streamlit.text('🥑 Banana, Grapes, Apples and Honey')
streamlit.text('🥗 Oatmeal and Milk')  
streamlit.header('Build your own fruit smoothie')

# Build a Sheet from CSV
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Set the name of fruit as index
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
streamlit.dataframe(my_fruit_list)
