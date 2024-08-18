import streamlit as st
import qrcode
from forms.macros import qr_code_gen, save_qrcode

text = st.text_input("Enter text to generate a QR-Code: ")

st.write("\n")

col1, col2 = st.columns(2, gap="small", vertical_alignment="top")

with col1:
    if text:
        st.write("This is your QR-Code: ")

with col2:
    if text:
        qr_img = qr_code_gen(text)
        file_name = save_qrcode(qr_img)
        st.image(file_name, caption="Generated QR-Code")