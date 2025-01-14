import streamlit as st
from matplotlib.colors import LinearSegmentedColormap

# Set the page configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="📋",
    layout="centered"
)

# Custom CSS for styling
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

# --------------------------------- SIDEBAR ---------------------------------
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
        text-decoration: none;
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
    <a href="https://www.linkedin.com/in/cakiiremre/" target="_blank" class="linkedin-icon">
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

# --------------------------------- SUMMARIZE ---------------------------------
# Main page title
st.markdown(
    """
    <div class='main-text-3'><i class="material-icons">person</i> Hi, I'm Emre Çakır – Data Analyst and Problem Solver!</div>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 class='main-title'>Summarize</h1>", unsafe_allow_html=True)
st.write("")
st.markdown(
    """
    <div class='main-text'> With over 2 years of experience in data analysis, I specialize in transforming complex datasets into actionable insights that drive business decisions. My expertise lies in:</div>
    """,
    unsafe_allow_html=True
)

# Main page content
st.markdown(
    """
    <div class='main-text-2'><i class="material-icons">check_circle</i> Data Analysis</div>
    <div class='main-text'>Proficient in SQL, Excel, and Python for data manipulation, cleaning, and statistical analysis.</div>
    <div class='main-text-2'><i class="material-icons">check_circle</i> Data Visualization</div>
    <div class='main-text'> Proficient in SQL, Excel, and Python for data manipulation, cleaning, and analysis.</div>
    <div class='main-text-2'><i class="material-icons">check_circle</i> Data Science</div>
    <div class='main-text'>Basic knowledge of Machine Learning and Deep Learning models, applying them to predictive analysis and feature engineering.</div>
    """,
    unsafe_allow_html=True
)



# --------------------------------- SKILLS ---------------------------------
import matplotlib.pyplot as plt

st.markdown("<h1 class='main-title'>Main Skills</h1>", unsafe_allow_html=True)

def new_func(num, tool, color, color_2):
    with num:
    # Create a rectangle using matplotlib
        fig, ax = plt.subplots()  # Define fig and ax properly

    # change the figsize of the plot
        fig.set_size_inches(2, 1)

    # Plotting the rectangle
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        ax.add_patch(plt.Rectangle((1, 2.5), 1, 1, edgecolor='white', facecolor='black', lw=1, alpha=0))

    # change the color of axis
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        
        cmap = LinearSegmentedColormap.from_list("custom_gradient", [color_2, color])
        
    # set the background color of the plot
        fig.patch.set_facecolor('lightgray') # change the background color of the plot
    # fig.patch.set_alpha(0)
        fig.patch.set_edgecolor(color_2) # change the color of the edge line
        ax.imshow([[0, 1], [0, 1]], cmap=cmap, interpolation='bicubic', aspect='auto', extent=[0, 10, 0, 6])
        fig.patch.set_alpha(0.9) # set the transparency of the edge line

        fig.patch.set_linewidth(5) # change the width of the edge line
        fig.patch.set_linestyle('solid') # change the style of the edge line
        fig.patch.set_antialiased(True) # render the edge line smooth 
        fig.patch.set_fill(False) # fill the background color
        fig.patch.set_hatch('/' ) # change the hatch style of the edge line
        fig.patch.set_visible(True) # set the visibility of the edge line
        # fig.patch.set_in_layout(True) # set the in layout of the edge line

    # change the color of graph background
        ax.set_facecolor(color_2)

        # Create a gradient background
        cmap = LinearSegmentedColormap.from_list("custom_gradient", [color_2, color])
        ax.imshow([[0, 1], [0, 1]], cmap=cmap, interpolation='bicubic', aspect='auto', extent=[0, 10, 0, 6])

    # Adding the text "Python" inside the rectangle
        ax.text(5, 3, tool, fontsize=14, ha='center', va='center', color='black')

    # Display the rectangle in Streamlit app
        st.pyplot(fig)

st.markdown(
    """
    <div class='main-subheading'></div>
    <div class='main-subheading'><i class="material-icons">bolt</i> Programming Tools:</div>
    """,
    unsafe_allow_html=True
)

one, two, three= st.columns(3)

new_func(one, 'Python', 'AntiqueWhite', 'yellowgreen') #rosybrown 
new_func(two, 'SQL', 'AntiqueWhite', 'BurlyWood')
new_func(three, 'Excel', 'AntiqueWhite', 'Chocolate')

st.markdown(
    """
    <div class='main-subheading'></div>
    <div class='main-subheading'><i class="material-icons">bolt</i> Visualization Tools:</div>
    """,
    unsafe_allow_html=True
)

four, five, six= st.columns(3)
new_func(four, 'Tableau', 'AntiqueWhite', 'CadetBlue')
new_func(five, 'Looker Studio', 'AntiqueWhite', 'CornflowerBlue')
new_func(six, 'Power BI', 'AntiqueWhite', 'DarkGoldenRod')

st.markdown(
    """
    <div class='main-subheading'></div>
    <div class='main-subheading'><i class="material-icons">bolt</i> Scientific Tools:</div>
    """,
    unsafe_allow_html=True
)

seven, eight, nine= st.columns(3)
new_func(seven, 'Machine\nLearning', 'AntiqueWhite', 'Gray')
new_func(eight, 'Deep\nLearning', 'AntiqueWhite', 'IndianRed')
new_func(nine, 'Statistics', 'AntiqueWhite', 'Lavender')



# --------------------------------- EXPERIENCE ---------------------------------

# Main page title
st.markdown("<h1 class='main-title'>Experience</h1>", unsafe_allow_html=True)
st.write("")



st.markdown(
    "<div class='custom-subheader'>Liorice (E-Commerce Store @Trendyol Group)</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='sub-text'>Data Analyst - Business Intelligence</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='sub-text'>May 2023 - Present</div>
    """,
    unsafe_allow_html=True
)

# Main page content
st.markdown(
    """
    <div class='main-text'></div>
    <div class='main-text'>- I have cleaned, transformed, and analyzed complex datasets using Python (Pandas, NumPy, Scikit-learn), SQL, and other tools. By developing predictive models, I forecasted future sales and optimized inventory management.</div>
    <div class='main-text'>- Using Looker Studio, Power BI and Tableau, I created compelling visualizations to clearly convey sales trends, customer behaviors, and business performance, which accelerated data-driven decision-making processes.</div>
    <div class='main-text'>- I conducted in-depth analyses and generated data-driven reports by integrating with Trendyol's sales platform database using Excel and SQL.</div>
    <div class='main-text'>- Through my work with SQL and Python, I developed an algorithm for "different shipping companies by region," reducing order delivery times and increasing customer satisfaction.</div>
    <div class='main-text'>- By implementing a dynamic pricing strategy, I achieved a significant increase in order numbers.</div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    "<div class='custom-subheader'>Projecture Architectural & Engineering</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='sub-text'>Project Engineer - Mechanical Engineer</div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class='sub-text'>September 2022 - April 2023</div>
    """,
    unsafe_allow_html=True
)
# Main page content
st.markdown(
    """
    <div class='main-text'></div>
    <div class='main-text'>- I had the opportunity to work on various projects, ranging from facilities to campuses, from living spaces to high-rise buildings.</div>
    <div class='main-text'>- I used 3D CAD programs such as AutoCAD MEP and MicroStation, as well as utilities like Solar Computer and Trox.</div>
    <div class='main-text'>- Focusing on the question, "Is it feasible in the field?", I performed calculations and created drawings for heating, ventilation, and sanitary systems to produce applicable projects.</div>
    <div class='main-text'>- I worked on projects that enhanced individual abilities such as problem-solving, improvement/development, teamwork, and decision-making under time pressure.</div>
    <div class='main-text'>- I provided training to my colleagues on the programs I learned, including MicroStation and Solar Computer.</div>
    """,
    unsafe_allow_html=True
)

# --------------------------------- CERTIFICATIONS ---------------------------------

# Main page title
st.markdown("<h1 class='main-title'>Certifications</h1>", unsafe_allow_html=True)
st.write("")

st.markdown(
    "<div class='custom-subheader'>IBM-Machine Learning Basics with Python</div>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class='main-text'><i class="material-icons">check</i>Coursera</div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.markdown(
    "<div class='custom-subheader'>Stanford-Supervised & Unsupervised Learning</div>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class='main-text'><i class="material-icons">check</i>Coursera</div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    "<div class='custom-subheader'>SQL for Data Analysis</div>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class='main-text'><i class="material-icons">check</i>LinkedIn</div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    "<div class='custom-subheader'>Intermediate SQL: Data Reporting and Analysis</div>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class='main-text'><i class="material-icons">check</i>LinkedIn</div>
    """,
    unsafe_allow_html=True
)


# --------------------------------- EDUCATION ---------------------------------

# Main page title
st.markdown("<h1 class='main-title'>Education</h1>", unsafe_allow_html=True)
st.write("")

st.markdown(
    "<div class='custom-subheader'>Mechanical Engineering</div>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class='main-text'><i class="material-icons">chevron_right</i>Akdeniz University</div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class='main-text'><i class="material-icons">chevron_right</i>Bachelor's Degree</div>
    """,
    unsafe_allow_html=True
)












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





# Footer
st.markdown(
    """
    <div class='text' style="text-align: center; font-size: 16px; margin-top: 40px;">
        Created with ❤️ using Streamlit 👨‍💻 by Emre Çakır
    </div>
    """,
    unsafe_allow_html=True
)