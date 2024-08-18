import streamlit as st
from forms.macros import contact_form

st.title("About me")
st.write("This is a hobby project. Filling the form below does not send me any e-mail.")

@st.dialog("Contact me")
def show_contact_form():
    contact_form()

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.title("Sokha Peng, BA", anchor=False)
    st.write("Data Analyst at Allianz")
    if st.button("Text me"):
        show_contact_form()

with col2:
    st.write("placeholder for picture")


st.write("\n")
st.title("My Playground", anchor=False)
st.write(
    """
    - SAS Enterprise (Statistical Analysis System)
    - Python
    - SQL
    - Power BI
    - Excel (including VBA)
    - Google Sheets (including Apps Script)
    """
)

st.write("\n")
st.title("Experience", anchor=False)
st.write(
    """
    - 7 years at Allianz
    - 1 year at WGKK
    - 4 months at Servotel
    """

)

st.write("\n")
st.title("Education", anchor=False)
st.write(
    """
    - Bachelor of Arts at FH Campus Wien University of Applied Sciences
    - Highschool at GRG3 Hagenmüllergasse
    """
)