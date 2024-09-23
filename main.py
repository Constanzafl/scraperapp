import streamlit as st

st.title("AI web scraper con llms")
url=st.text_input("Enter the URL:")

if st.button("Srape Site"):
    st.write("Scraping site now")

