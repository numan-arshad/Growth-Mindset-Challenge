#streamlit
import streamlit as st

st.set_page_config(page_title= "Growth Mindset Project")
st.title("⌛Growth Mindset Challenge: Web App with Streamlit")

st.header("Welcome to Your Growth Journey!")
st.write("Take on challenges, learn from your mistakes, and unlock your true potential. This AI-app helps you build a growthful mindset through reflection, challenges, and celebrating your progress!.✌")

#Quote
st.header("Growth Mindset Quote🌺")
st.write("Success is not how high you have climbed, but how you make a positive difference to the world. _Roy T. Bennett")
st.header("What's your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input:
    st.success(f" You're facing: {user_input}. Keep going towards your goal, CHAMP!")
else:
    st.warning("Tell us about the difficulties you're facing to get started!")  

#reflecting
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection}✨")
else:
    st.info("Reflecting on past experience will help you grow. so just share your difficulties.")   

#achievements
st.header("Celebrate your Wins❤️️")
achievements = st.text_input("Share something that you have recently accomplished.")

if achievements:
    st.success(f"WOW! You have achieved⭐: {achievements}")
else:
    st.info("Failure is not the opposite of success, it's part of success.")

#footer
st.write("- - -")
st.write("The harder you work for something. The greater you will feel when you achieve it.")
st.write("Created by Numan Arshad")
st.write("(Student of giaic)")