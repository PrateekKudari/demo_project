import streamlit as st

st.title("Simple User Input Form")

# Input fields
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120)
dob = st.date_input("Select your date of birth")

# Submit button
if st.button("Submit"):
    st.write("### User Details")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Date of Birth:** {dob}")
