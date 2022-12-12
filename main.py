
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

st.write("Welcome to the Say Yes Project")
st.write("Where you can keep tracj of all of your ideas for upcoming Nuptules!")
# print("Welcome to the Say Yes Project, where you can keep track of all of your ideas for your wedding!")
