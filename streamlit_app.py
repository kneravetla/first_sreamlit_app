import streamlit
import requests
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner');

streamlit.header ('Breakfast Menu');

streamlit.text ( " 🥣 Omega 3 & BlueBerry OatMeal" );
streamlit.text ( " 🥗 Kale, Spinach & Rocket Smoothie" );
streamlit.text ( " 🐔 Hard Boiled Free-Range Egg" );
streamlit.text ( " 🥑🍞 Avacado Toast" );

streamlit.header ('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');



#
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit');
fruits_selected = streamlit.multiselect("Pick Some Fruits:", my_fruit_list.index, ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the table on page
streamlit.dataframe(fruits_to_show);

#create the repetable code block (function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json());
    return fruityvice_normalized
    
# New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = streamlit.text_input('What Fruit would you like information about?')
    if not fruit_choice :
         streamlit.error('Please select a fruit to get information')
    else: 
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function);
except URLError as e:
    streamlit.error()

streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall();
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# New Section to display fruityvice api response
streamlit.header('What Fruit Would you like to add?');
fruit_to_add = streamlit.text_input('What Fruit Would you like to add?');
streamlit.write('Thanks for adding' ,  fruit_to_add)

my_cur.execute("insert into fruit_load_list values ('from streamlit')");

