import streamlit as st
import os

def Home():
# Show title and description.
    st.title("Jaida's Publicly-Available Work")
    st.header("Personal Projects (Ongoing Work)")
    st.page_link("culturewarftp.py", label="The Culture War for the Planet", icon="🌎")
    st.markdown("Comparative analysis of popular climate-related subreddits")
    st.markdown("**Helping me learn:** Intermediate Natural Language Processing - Topic Modeling, Semantic Similarity Analysis")
    st.page_link("logicbot.py", label="LogicBot", icon='🦾')
    st.markdown("Argument-Strength Analyzer _(takes a few seconds to load!)_")
    st.markdown("**Helping me learn:** Basic Natural Language Processing (tokenization, lemmatization, noun phrase chunking); applied logic")
    st.divider()
    st.header("Institutional Work")
    st.markdown("**Surfing the Kali Yuga: Tracking the Alt-Right on Twitter (2023)**")
    st.markdown("*Bowdoin College Digital Commons*")
    st.markdown("[Abstract](https://digitalcommons.bowdoin.edu/honorsprojects/431/) | [Download Link](https://digitalcommons.bowdoin.edu/cgi/viewcontent.cgi?article=1472&context=honorsprojects)")
    st.markdown("**How 'Don't Say Gay' Bills Harm our Youth (2022)**")
    st.markdown("*Op-Ed, Bangor Daily News*")
    st.markdown("[News Link](https://www.bangordailynews.com/2022/07/26/opinion/opinion-contributor/harmful-dont-say-gay-bills-opinion-joam40zk0w/)")

pages = [st.Page(Home, default=True), st.Page("culturewarftp.py", title="Culture War for the Planet"), st.Page("logicbot.py", title="LogicBot"), st.Page("climate_conscious_comp.py", title="Climate-Conscious Computation")]
pg = st.navigation(pages)
pg.run()

#os.system("streamlit run streamlit_app.py")
