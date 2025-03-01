import streamlit as st


def load_css():
    with open("style.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category


st.title("⚖️ BMI Calculator")
load_css()


weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (m)", min_value=0.5, step=0.01)

if st.button("Calculate BMI", key="bmi_btn"):
    if height > 0:
        bmi, category = calculate_bmi(weight, height)
        st.success(f"Your BMI: {bmi:.2f}")
        st.info(f"Category: {category}")
    else:
        st.error("Height must be greater than 0!")
