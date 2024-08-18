import streamlit as st

# set pages 
home_page = st.Page(
    page = "views/home.py",
    title = "Homepage",
    icon = "🏠",
    default = True,
)

contact_page = st.Page(
    page = "views/contact.py",
    title = "Contact me",
    icon = "✉️",
)

aboutme_page = st.Page(
    page = "views/aboutme.py",
    title = "About me",
    icon = "🌞",
)

qrgen_page = st.Page(
    page = "views/qrgen.py",
    title = "QR Code Generator",
    icon = "📝",
)

# set navigation
#pg = st.navigation(pages=[home_page, contact_page])

pg = st.navigation(
    {
    "General" : [home_page, aboutme_page],
    "Projects" : [qrgen_page],
    "Forms" : [contact_page]
    }
)

st.sidebar.text("Made with love by Sokha ❤️")

pg.run()