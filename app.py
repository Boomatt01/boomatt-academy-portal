import streamlit as st

st.set_page_config(
    page_title="Boomatt Academy",
    page_icon="📚"
)

st.title("Boomatt Academy")
st.subheader("Building Confident Learners, One Lesson at a Time")

st.write("Welcome to the Boomatt Academy Portal.")

role = st.selectbox(
    "Who are you?",
    ["Admin", "Tutor", "Parent", "Student"]
)

st.write(f"You selected: {role}")
