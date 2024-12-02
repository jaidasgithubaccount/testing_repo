import streamlit as st
from openai import OpenAI


# Show title and description.
st.title("Jaida's Publicly-Available Work")
st.header("Institutional Work")
st.markdown('''
    **Surfing the Kali Yuga: Tracking the Alt-Right on Twitter (2023)**
    *Bowdoin College Digital Commons*
             
    [Abstract](https://digitalcommons.bowdoin.edu/honorsprojects/431/) | [Download Link](https://digitalcommons.bowdoin.edu/cgi/viewcontent.cgi?article=1472&context=honorsprojects)        
            ''')
st.markdown(
    '''
    **How 'Don't Say Gay' Bills Harm our Youth (2022)**
    *Op-Ed, Bangor Daily News*

    [News Link](https://www.bangordailynews.com/2022/07/26/opinion/opinion-contributor/harmful-dont-say-gay-bills-opinion-joam40zk0w/) 
    '''
)
st.header("Personal Projects")
st.page_link("pages/culturewarftp.py", label="The Culture War for the Planet")
st.page_link("pages/logicbot.py", label="LogicBot")


