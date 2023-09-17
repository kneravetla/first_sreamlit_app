import streamlit

streamlit.title('My Parents New Healthy Diner');

streamlit.header ('Breakfast Menu');

streamlit.text ( " 🥣 Omega 3 & BlueBerry OatMeal" );
streamlit.text ( " 🥗 Kale, Spinach & Rocket Smoothie" );
streamlit.text ( " 🐔 Hard Boiled Free-Range Egg" );
streamlit.text ( " 🥑🍞 Avacado Toast" );

streamlit.header ('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');

import pandas;

#
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit');
fruits_selected = streamlit.multiselect("Pick Some Fruits:", my_fruit_list.index, ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table on page
streamlit.dataframe(fruits_to_show);

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon");
streamlit.text(fruityvice_response.json())

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json());
streamlit.dataframe(fruityvice_normalized);
