import re
import streamlit as st
import qrcode

def validate_email(email):
    email_reg = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_reg, email):
        return True
    else:
        return False
    
def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your E-Mail Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:

            if not name:
                st.error("Please enter your name!")
                st.stop()

            if not email:
                st.error("Please enter your e-mail address!")
                st.stop()

            if validate_email(email) == False:
                st.error("Please enter a correct e-mail address!")
                st.stop()

            if not message:
                st.error("Please provide a message!")
                st.stop()

            st.success("Message sent!")
            
            #data = {"name" : name, "email" : email, "message" : message}

def qr_code_gen(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    return img

def save_qrcode(img, filename="assets/qrcode.png"):
    img.save(filename)
    return filename
    