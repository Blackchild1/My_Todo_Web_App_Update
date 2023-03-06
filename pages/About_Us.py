import time

import streamlit as st
import functions
import os


st.set_page_config(
    page_title="About Us",
    page_icon="✍",
)

st.write("# Welcome to TopG Todo App! 👋")
st.markdown(
    """
    This app main purpose is to help increase your productivity as an 
    individual.

    **👈 You can always read notes on your todos through the 
    sidebar!

    ### Want to add todos?          

    - Use the input box below                    
    - Type your todo and press enter                
    - **Done


    ### Wanna checkout todos?
    - Use the checkbox 
    - Then it moves to completed  

   """
)