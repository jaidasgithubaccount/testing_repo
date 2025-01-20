import streamlit as st

# Show title and description.
st.title("The Culture War for the Planet 🌎")
st.header('Comparative analysis of Reddit forums r/collapse, r/preppers, r/itcouldhappenhere, r/climate and r/climatechange', divider="blue")

left, middle, right = st.columns([0.15, 0.7, 0.15])
with middle:
  st.link_button(label="Redditors' Takes on the Climate Catastrophe", url="https://jaidasgithubaccount.github.io/data_visualizations/", icon='📊', use_container_width=True)