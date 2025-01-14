import streamlit as st
from streamlit_option_menu import option_menu


# Custom CSS for styling the page elements
st.markdown(
"""
<style>
/* Change background color */
.stApp {
    background-color: #202020; /* Light grayish blue */
}

/* Title styling */
.title {
    font-size: 32px;
    font-weight: bold;
    color: #4CAF50; /* Green color */
    text-align: left; # center
    margin-top: 0px;
}

/* Title styling with underline */
.title-under-line {
    font-size: 22px;
    font-weight: bold;
    color: #CFCFCF;
    position: relative;
    padding-bottom: 0px;
}
.title-under-line::after {
    content: '';
    display: block;
    width: 10%;
    height: 3px;
    background-color: #4CAF50;
    position: absolute;
    bottom: -8px;
}
/* Subtitle styling */
.subtitle {
    font-size: 24px;
    font-weight: semi-bold;
    color: #CFCFCF; /* Dark gray */
    text-align: left; # center
    margin-top: 10px;
}

/* Regular text styling */
.text {
    font-size: 18px;
    color: #888888; /* Medium gray */
    text-align: justify;
    line-height: 1.6;
    margin: 10px auto;
    width: 100%;
}

/* Colorful result box - 1 */
.result-box {
    background-color: #BDB76B;
    border: 2px solid #e9ecef;
    padding: 15px;
    border-radius: 10px;
    font-family: Arial, sans-serif;
    font-size: 18px;
    color: #212529;
    line-height: 1.6;
    padding-bottom: 0px;
}

/* Colorful result box - 2 */
.result-box-2 {
    background-color: #000000;
    border: 2px solid #e9ecef;
    padding: 15px;
    border-radius: 10px;
    font-family: Arial, sans-serif;
    font-size: 18px;
    color: #ffffff;
    line-height: 1.6;
    padding-bottom: 0px;
}
</style>
""",
unsafe_allow_html=True
)


st.markdown(f"<div class='title'>My Public Tableau Portfolio</div>", unsafe_allow_html=True)
# Sub-title
st.markdown("<div class='subtitle'>You can access the dashboards below and much more.</div>", unsafe_allow_html=True)
st.write("")
st.write("----------------")

first, second, third = st.columns([10, 0.5, 10])

with first:

    st.image("pages/dashboard-1.JPG", use_container_width =True)
    st.markdown(
        """
        <style>
        .stImage img {
            border-radius: 15px; /* Adjust the value to change the curve */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

with third:
    st.markdown(f"<div class='title' style='color: pink; font-size: 22px; text-align: center;'>Superstore Dashboard - 1</div>", unsafe_allow_html=True)
    # Summary of the model
    st.markdown(
        """
        <div class='text'>
            I wanted to present you some of the graphs I obtained using data such as sales, profit and 
            quantity of a superstore. You can use the country filter to get more detailed information about the chart you want.
        </div>
        """,
        unsafe_allow_html=True
    )

# Stil ve buton yerleşimi
st.markdown("""
    <style>
    .centered-button {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px; /* Butonun çevresindeki boşluk */
    }
    .button-container {
        display: inline-block;
        text-align: center;
    }
    .button-container a {
        background-color: #4CAF50; /* Buton rengi */
        color: white; /* Yazı rengi */
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
        font-size: 18px;
        font-family: Arial, sans-serif;
    }
    .button-container a:hover {
        background-color: #45a049; /* Hover rengi */
    }
    </style>
    <div class="centered-button">
        <div class="button-container">
            <a href="https://public.tableau.com/app/profile/emre.cakir4757/viz/SuperStore_17141859123050/Dashboard1" target="_blank">
                View Tableau Dashboard
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("----------------")



ff, ss , jj = st.columns([10, 0.5, 10])

with ff:

    st.image("pages/dashboard-2.JPG", use_container_width =True)
    st.markdown(
        """
        <style>
        .stImage img {
            border-radius: 15px; /* Adjust the value to change the curve */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Stil ve buton yerleşimi
st.markdown("""
    <style>
    .centered-button {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px; /* Butonun çevresindeki boşluk */
    }
    .button-container {
        display: inline-block;
        text-align: center;
    }
    .button-container a {
        background-color: #4CAF50; /* Buton rengi */
        color: white; /* Yazı rengi */
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
        font-size: 18px;
        font-family: Arial, sans-serif;
    }
    .button-container a:hover {
        background-color: #45a049; /* Hover rengi */
    }
    </style>
    <div class="centered-button">
        <div class="button-container">
            <a href="https://public.tableau.com/app/profile/emre.cakir4757/viz/SuperStore-Blade_Runner2/Dashboard3" target="_blank">
                View Tableau Dashboard
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("----------------")

with jj:
    st.markdown(f"<div class='title' style='color: pink; font-size: 22px; text-align: center;'>Superstore Dashboard - 2</div>", unsafe_allow_html=True)
    # Summary of the model
    st.markdown(
        """
        <div class='text'>
            A dashboard where I focused on various visualization tools and color diversity to create a more readable presentation. 
            You can enjoy exploring this dashboard, which incorporates advanced charting techniques.
        </div>
        """,
        unsafe_allow_html=True
    )



st.markdown(
"""
<style>
/* Change background color */
.stApp {
    background-color: #202020; /* Light grayish blue */
}

/* Title styling */
.title {
    font-size: 32px;
    font-weight: bold;
    color: #4CAF50; /* Green color */
    text-align: left; # center
    margin-top: 0px;
}

/* Title styling with underline */
.title-under-line {
    font-size: 22px;
    font-weight: bold;
    color: #CFCFCF;
    position: relative;
    padding-bottom: 0px;
}
.title-under-line::after {
    content: '';
    display: block;
    width: 10%;
    height: 3px;
    background-color: #4CAF50;
    position: absolute;
    bottom: -8px;
}
/* Subtitle styling */
.subtitle {
    font-size: 24px;
    font-weight: semi-bold;
    color: #CFCFCF; /* Dark gray */
    text-align: left; # center
    margin-top: 10px;
}

/* Regular text styling */
.text {
    font-size: 18px;
    color: #888888; /* Medium gray */
    text-align: justify;
    line-height: 1.6;
    margin: 10px auto;
    width: 100%;
}

/* Colorful result box - 1 */
.result-box {
    background-color: #BDB76B;
    border: 2px solid #e9ecef;
    padding: 15px;
    border-radius: 10px;
    font-family: Arial, sans-serif;
    font-size: 18px;
    color: #212529;
    line-height: 1.6;
    padding-bottom: 0px;
}

/* Colorful result box - 2 */
.result-box-2 {
    background-color: #000000;
    border: 2px solid #e9ecef;
    padding: 15px;
    border-radius: 10px;
    font-family: Arial, sans-serif;
    font-size: 18px;
    color: #ffffff;
    line-height: 1.6;
    padding-bottom: 0px;
}
</style>
""",
unsafe_allow_html=True
)


# Footer
st.markdown(
    """
    <div class='text' style="text-align: center; font-size: 16px; margin-top: 40px;">
        Created with ❤️ using Streamlit 👨‍💻 by Emre Çakır
    </div>
    """,
    unsafe_allow_html=True
)


















# ----------------- SIDEBAR -----------------
st.markdown(
    """
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
    /* Custom CSS for sidebar titles and text */
    .sidebar-title {
        font-size: 26px;
        line-height: 1.6;
        color: white;
        font-family: Verdana, sans-serif;
        padding-bottom: 10px;
        font-weight: bold;
    }
    .sidebar-text {
        font-size: 24px;
        line-height: 1.6;
        color: white;
        font-family: Verdana, sans-serif;
        font-weight: bold;
    }
    .sidebar-subtext {
        font-size: 18px;
        line-height: 1.6;
        color: white;
        font-family: Verdana, sans-serif;
        padding-bottom: 10px;
        font-style: italic;
    }
    /* Main page title styling */
    .main-title {
        color: #4CAF50;
        border-bottom: 3px solid #4CAF50;
        padding-bottom: 5px;
        width: 100%;
        margin: 0 auto;
        display: inline-block;
    }
    .main-text-2 {
        font-size: 18px;
        line-height: 1.6;
        color: #CFCFCF;
        font-family: Verdana, sans-serif;
        padding-bottom: 10px;
        display: flex;
        align-items: center;
        font-weight: bold;
    }
    .main-subheading {
        font-size: 24px;
        line-height: 1.6;
        color: #CFCFCF;
        font-family: Verdana, sans-serif;
        padding-bottom: 10px;
        display: flex;
        align-items: center;
    }
    .main-text-3 {
        font-size: 18px;
        line-height: 1.6;
        color:#CFCFCF;
        font-family: Verdana, sans-serif;
        padding-bottom: 10px;
        display: flex;
        align-items: center;
        font-weight: bold;
    }
    /* Main page content styling */
    .main-text {
        font-size: 18px;
        line-height: 1.6;
        color: #888888;
        font-family: Verdana, sans-serif;
        padding-bottom: 10px;
        display: flex;
        align-items: center;
    }
    .material-icons-green {
        font-size: 18px;
        color: #4CAF50; /* Green */
        margin-right: 8px;
    }
    .material-icons {
        font-size: 18px;
        color: #4CAF50;
        margin-right: 8px;
    }
    /* Sidebar background styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #000000, #5A6C57, #000000);
        color: white;
    }
    /* Sidebar text styling */
    [data-testid="stSidebar"] .css-1d391kg {
        color: white;
        font-size: 16px;
    }
    /* Main app background color */
    .stApp {
        background-color: #202020;
    }
    /* Main sub text styling */
    .sub-text {
        font-size: 16px;
        line-height: 1.6;
        color: #CFCFCF;
        font-family: Verdana, sans-serif;
        font-style: italic;
    }
    .custom-subheader {
        font-size: 24px; /* Adjust font size */
        color: #CFCFCF; /* Change color to green */
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar title
st.sidebar.markdown("<div class='sidebar-title'>About Me</div>", unsafe_allow_html=True)

# Add an image to the sidebar
st.sidebar.image("PROFILE PHOTO/emre-photo.jpg", use_container_width=True)

# Job Title and Name
st.sidebar.markdown(
    """
    <div class='sidebar-text'>Emre Çakır</div>
    <div class='sidebar-subtext'>Data Analyst - Mechanical Engineer</div>
    """,
    unsafe_allow_html=True
)

# Sidebar content
if st.sidebar.checkbox("Phone Number"):
    st.sidebar.info("+90 551 020 47 49")
if st.sidebar.checkbox("E-mail"):
    st.sidebar.info("cakiiremre@hotmail.com")


# Custom CSS for styling
st.markdown(
    """
    <style>
    .linkedin-icon {
        font-size: 20px;
        color: #0077B5;
        text-decoration: none !important;
        display: flex;
        align-items: center;
        margin-right: 20px;
    }
    .linkedin-icon:hover {
        color: #005582;
    }
    .linkedin-icon i {
        margin-right: 8px;
        color: #0077B5; /* Change the color of the icon */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# LinkedIn icon and link
st.sidebar.markdown(
    """
    <a href="https://www.linkedin.com/in/cakiiremre/" target="_blank" class="linkedin-icon">
        <i class="material-icons">link</i> 
        LinkedIn Profile
    </a>
    """,
    unsafe_allow_html=True
)

# LinkedIn icon and link
st.sidebar.markdown(
    """
    <a href="https://github.com/RavenWave" target="_blank" class="linkedin-icon">
        <i class="material-icons">link</i> 
        GitHub Profile
    </a>
    """,
    unsafe_allow_html=True
)

st.sidebar.write("")
resume_file_path = "RESUMES/Data Analyst Resume.pdf"
resume_file_path_t = "RESUMES/Veri Analisti Resume.pdf"

# Read the resume file
with open(resume_file_path, "rb") as file:
    resume_data = file.read()

with open(resume_file_path_t, "rb") as file:
    resume_data_t = file.read()

# Create a download button
st.sidebar.download_button(
    label="Download My Resume in English",
    data=resume_data,
    file_name="Emre_Cakir_Resume.pdf",
    mime="application/pdf",
    key="download-button",
    help="Click to download my resume",
)

st.sidebar.download_button(
    label="Download My Resume in Turkish",
    data=resume_data_t,
    file_name="Emre_Cakir_Resume.pdf",
    mime="application/pdf",
    key="download-button-2",
    help="Click to download my resume",
)