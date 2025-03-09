import streamlit as st 
import re 

st.set_page_config(page_title="Password Strenght Checker", page_icon="🔒")

st.title("🔐 Password Strenght Checker")
st.markdown("""
## welcome to the ultimate password strenght checker!👋
use this simple tool to check the strenght of your password and get suggestions on how to make it stronger.
we will give you helpful tips to create a **Stronge Password** 🔒""")

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("❌Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else :
        feedback.append("❌Password should contain both uppercase and lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else :
        feedback.append("❌Password should contain at least one number.")

    if re.search(r'[!@#$%&*]', password):
        score += 1
    else :
        feedback.append("❌Password should contain at least one special character(!@#$%&*).")
    if score == 4:
        feedback.append("✅ Your password is Strong!🎉")
    elif score == 3:
        feedback.append("🌕 Your password is medium strenght. It could be stronger.")
    else:
        feedback.append("🔴 Your password is Weak. Try to make it stronger.")

    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter a password to get started.")