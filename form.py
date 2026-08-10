import streamlit as st
from datetime import date
from datetime import timedelta

today_date = date.today()
min_age = 16
max_date_cutoff = today_date - timedelta(days=min_age * 365)


st.title("Course signup form")
st.header("Fill out form below to signup for the course")

user_name = st.text_input("Enter your name:")
description = st.text_area("Enter brief description on expectations from this course:")
dob = st.date_input(
    "Select Your Date Of Birth", min_value="1930-01-01", max_value=max_date_cutoff
)
gender = st.radio("Choose Your Gender", ("Male", "Female", "Others"), horizontal=True)
courses = ["python", "DataScience", "Django", "SQL"]
course_chosen = st.multiselect("Select couse to enroll", courses)
agreed = st.checkbox("I agree to the terms and conditions")
if agreed:
    signup_button_clicked = st.button("SignUp")
    if signup_button_clicked:
        if not user_name:
            st.error("please enter your name.")
        else:
            st.success(f"ThankYou {user_name} for signing up. Check Email for OTP.")
