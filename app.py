import streamlit as st

# Title of the app
st.title("Project Text Display")

# Read a display-only text file
try:
    with open("display.txt", "r") as file:
        content = file.read()

    st.subheader("Here is your message:")
    st.code(content, language='text')

except FileNotFoundError:
    st.error("File not found. Please upload it to the project directory.")

