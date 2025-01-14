import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Multipage App",
    page_icon=":bar_chart:",
    layout="wide"
)

# Define functions for each page
def home_page():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def page1():
    st.title("Page 1")
    st.write("This is Page 1.")

def page2():
    st.title("Page 2")
    st.write("This is Page 2.")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Page 1", "Page 2"])

# Display the selected page
if page == "Home":
    home_page()
elif page == "Page 1":
    page1()
elif page == "Page 2":
    page2()

# Additional sidebar content (optional)
st.sidebar.success("Select a page above.")