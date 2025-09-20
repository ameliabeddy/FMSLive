import streamlit as st

# Title of the app
st.title("Project Requirements")

# Read the requirements.txt file
try:
    with open("requirements.txt", "r") as file:
        requirements = file.read()

    # Display in a code block
    st.subheader("Dependencies (from requirements.txt):")
    st.code(requirements, language='text')

except FileNotFoundError:
    st.error("requirements.txt file not found. Please upload it to the project directory.")
