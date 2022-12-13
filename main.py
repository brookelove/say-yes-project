
'''
1. welcome user to the say yes project
2. then prompt user for their desired wedding date, location, your and partners name, budget
    CLASS:  
    - inform them that they can change the date later 
    - TRY / ELSE BLOCK where i am trying ot get a valid date that is greater than the current day
    - while loop to ask for a valid date until it is not needs to be in a particular format MM/DD/YYYY and compare that it has to be greater than current date
3. click on options that you want to pick [elopement, big wedding, micro wedding]
    - confirm this what they want yes / no
4. have a dictionary comprised of lists that a person can add informaiton such as venue, food, bridal shops, tux, pinterst board links, color scheme 
    - can look at a table that shows the information 
    - cna delete the data if needed (will need to add an id of sorts or can just need to get the index)
5. output a file of the list of elements that the person has added 
'''
import streamlit as st
from datetime import date
st.title("Welcome to the Say Yes Project")
st.subheader(
    "Where you can keep track of all of your ideas for upcoming Nuptules!")
st.button(label="YES")
# print("Welcome to the Say Yes Project, where you can keep track of all of your ideas for your wedding!")

user_name = st.text_input("What is Your name?")
print(user_name)
partner_name = st.text_input("What is your Partner's name?")
print(partner_name)

today = date.today()
wedding_date = st.date_input(
    "What is your projected date you want to get married? (YYYY/MM/DD)", min_value=today)
wedding_date.strftime("%d/%m/%y")
location = st.text_input(
    "Do you know where you want to get married?")

print(wedding_date)
# ---------  this is where the table begins to get generated
st.button(label="NEXT")
# make a list of options thhey can pick on in a while loop until they click the word generate my list!

random_thoughts = st.text_area("What are some of your random thoughts?")
st.button("ENTER MY PLACES")

list_options = st.selectbox(
    'What category fits your inspiration?', ['Venue', 'Dress', 'Food', 'Flowers', 'Colors', 'Desserts'])
done = st.button("IM DONE")
