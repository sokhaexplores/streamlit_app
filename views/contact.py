import streamlit as st
from forms.macros import contact_form

st.title("✉️ Contact me")
st.write("This is a hobby project. Filling the form below does not send me any e-mail.")

contact_form()