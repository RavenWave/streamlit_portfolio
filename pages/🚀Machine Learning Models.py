import streamlit as st
from streamlit_option_menu import option_menu

# Horizontal Menu
selected = option_menu(
        menu_title="Machine Learning Models", #required
        options=["Regression: Car Price Prediction Model", 
                 "Regression: CO2 Emissions Prediction Model", 
                 "Classification: Heart Disease Prediction Model"], #required
        icons=["1-circle", "2-circle", "3-circle"], #optional (isimlerin yanına ikon eklemek için)
        menu_icon="globe", # optional
        default_index=0, #optional
        orientation = "horizontal", #optional
        # önce alttaki styles bolumu olmadan sayfayı run edin
        #sonra styles kullanarak farkı görun
        styles={
                "container": {"padding": "10!important", 
                              "background-color": "#202020",
                              "border-radius": "0px"},    
                "icon": {"color": "orange", 
                         "font-size": "18px"},
                "nav-link": {
                    "font-size": "18px",
                    "text-align": "left",
                    "margin": "10px",
                    "width": "650px",
                    "--hover-color": "green",
                    "border-radius": "50px"
                },
                "nav-link-selected": {"background-color": "green", 
                                      "color": "white", 
                                      "margin": "10px", 
                                      "border-radius": "50px", 
                                      "box-shadow": "0 0 7px 0 #ffffff"},
            },
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

# Create a button to make a prediction with custom color
button_style = """
<style>
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #000000;
}
.stButton>button:active {
    background-color: #000000;
}
</style>
"""



# ----------------- Page 1: Car Price Prediction Model-----------------
if selected == "Regression: Car Price Prediction Model": 

    # Title 1
    st.markdown(f"<div class='title'>Welcome to Car Price Prediction Model</div>", unsafe_allow_html=True)

    # Sub-title
    st.markdown("<div class='subtitle'>A Linear Regression Model</div>", unsafe_allow_html=True)

    # Summary of the model
    st.markdown(
        """
        <div class='text'>
            The Car Purchase Amount Prediction Model is a machine learning solution designed to 
            estimate the amount a customer is likely to spend on purchasing a car. 
            This predictive model leverages historical data and key customer attributes to provide actionable 
            insights for businesses in the automotive sector.
        </div>
        """,
        unsafe_allow_html=True
    )

    # import image
    im, ge, re= st.columns([1, 3, 1])
    with ge:
        st.image("pages/dalle.jpg", use_container_width =True)
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

    # Explanation for the model [Objective, Key Features, Machine Learning Technique]
    st.markdown(
        """
        <div class='text'>
            <strong>Objective:</strong>
            <ul>
                <li>Predict the car purchase amount based on customer demographic and financial information, 
                enabling dealerships to target the right customers with personalized offers.</li>
            </ul>
            <strong>Key Features:</strong>
            <ul>
                <li>Gender</li>
                <li>Age</li>
                <li>Annual Salary</li>
                <li>Credit Card Debt</li>
                <li>Net Worth</li>
            </ul>
            <strong>Machine Learning Technique:</strong>
            <ul>
                <li>Linear Regression</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Title 2
    st.markdown(f"<div class='title'>Make Some Prediction</div>", unsafe_allow_html=True)

    gender, age = st.columns(2)

    # Gender Selection Block
    with gender:
        # Gender Selection Title
        st.markdown("<div class='title-under-line'>Gender Selection:</div>", unsafe_allow_html=True)

        # Create a selectbox
        gender = st.selectbox(
            label="",
            options=["Male", "Female"],  # Options to choose from
            index=None,  # Default selected option
            help="Please select your gender",  # Help text displayed below the selectbox
            placeholder="Choose your gender...",  # Text displayed when no option is selected          
        )
        if gender == None:
            st.error("Please select your gender.")
        else:
            st.info(f"Your gender is {gender}")

    # Age Selection Block
    with age:
        # Age Selection Title
        st.markdown("<div class='title-under-line'>Age Selection:</div>", unsafe_allow_html=True)

        # Create an area for age input
        age = st.number_input(
            label="",
            min_value=18,  # Minimum value
            max_value=70,  # Maximum value
            value=None,  # Default value
            step=1,  # Step size
            format="%d",  # Format of the value
            help="Please enter your age",  # Help text displayed below the input area
        )
        if age == None:
            st.error("Please enter your age.")
        else:
            st.info(f"Your age is {age}")

    st.write("---------")

    # Annual Salary Selection
    st.markdown("<div class='title-under-line'>Annual Salary Selection:</div>", unsafe_allow_html=True)
    
    # Annual Salary slider
    annual_salary = st.slider(
        label="",
        min_value=20000,  # Minimum value
        max_value=1000000,  # Maximum value
        value=None,  # Default value
        step=10000,  # Step size
        format="%d",  # Format of the value as an integer
        help="""
        Please select your annual salary
        
        - Annual salary is the total amount of money earned from a job in a year.
        """,  # Help text displayed below the slider
    )

    # Change the format of salary
    def format_salary(value):
        """Formats the slider value with dots for thousands (e.g., 2.000.000)."""
        return f"{value:,}".replace(",", ".")
    
    st.info(f"Your Annual Salary is selected as {format_salary(annual_salary)}$")

    st.write("---------")

    cc, nw = st.columns(2)

    # Credit Card Dept Block
    with cc:
        # Credit Card Debt Selection
        st.markdown("<div class='title-under-line'>Credit Card Debt Selection:</div>", unsafe_allow_html=True)

        credit_card_debt = st.text_input(
            label="",
            value="",  # Default value
            max_chars=10,  # Maximum number of characters allowed
            help="Please enter your credit card debt",  # Help text displayed below the input area
            placeholder="Enter your credit card debt...",  # Placeholder text
        )

        # Validate the input to ensure it's a number
        if credit_card_debt:
            try:
                c_c_debt = int(credit_card_debt)
                st.info(f"Your Credit Card Debt is selected as {format_salary(c_c_debt)}$")
            except ValueError:
                st.error("Please enter a valid number for credit card debt.")
        else:
            st.error("Please enter your credit card debt.")

    # Net Worth Block
    with nw:
        # Net Worth Selection
        st.markdown("<div class='title-under-line'>Net Worth Selection:</div>", unsafe_allow_html=True)

        net_worth = st.text_input(
            label="",
            value="",  # Default value
            max_chars=10,  # Maximum number of characters allowed
            help="""
            Please enter your net worth 
            
            - Net worth is the total value of assets minus the total value of liabilities.
            """,  # Help text displayed below the input area
            placeholder="Enter your net worth...",  # Placeholder text
        )

        # Validate the input to ensure it's a number
        if net_worth:
            try:
                n_w = int(net_worth)
                st.info(f"Your Credit net worth is selected as {format_salary(n_w)}$")
            except ValueError:
                st.error("Please enter a valid number for net worth.")
        else:
            st.error("Please enter your net worth.")
    
    st.write("---------")
    
    # Linear Regression Model
    import joblib
    import pandas as pd

    # Load the model
    with open('Car_Price_Prediction.pkl', 'rb') as f:
        loaded_pipeline = joblib.load(f)

    # Convert the type of Gender into integer
    if gender == "Male":
        gender_num = 0
    elif gender == "Female":
        gender_num = 1
    else:
        gender_num = 2
    
    # Create a dataframe
    new_data = {
    "gender": gender_num,
    "age": age,
    "annual_Salary": annual_salary,
    "credit_card_debt": credit_card_debt,
    "net_worth": net_worth
}

    st.markdown(button_style, unsafe_allow_html=True)

    if st.button("Predict Car Price"):
        if new_data:
            try:
                if gender_num != 2:
                    new_df = pd.DataFrame(data=new_data, index=["Values"])
                    new_y_pred = loaded_pipeline.predict(new_df)
                    if new_y_pred < 0:
                        st.error("Car purchasing seems not possible according to these values above.", icon=":material/warning:")
                    else:
                        first, second = st.columns([2, 1])  # Adjust the width ratio of the columns
                        with first:
                            st.success("Prediction is made!", icon=":material/thumb_up:")

                            st.markdown(
                                f"""
                                <div class="result-box">
                                <strong>Your Inputs:</strong><br>
                                <ul>
                                    <li><strong>Age:</strong> {age}</li>
                                    <li><strong>Gender:</strong> {gender}</li>
                                    <li><strong>Net Worth:</strong> {format_salary(int(net_worth))}$</li>
                                    <li><strong>Annual Salary:</strong> {format_salary(annual_salary)}$</li>
                                    <li><strong>Credit Card Debt:</strong> {format_salary(int(credit_card_debt))}$</li>
                                </ul>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )  

                            st.write("")

                            st.markdown(
                                f"""
                                <div class="result-box-2">
                                Estimated car purchase amount:
                                <ul>
                                    <h4><strong>{format_salary(round(new_y_pred[0]))}$</strong></h4>
                                </ul>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )


                            # st.success(f"Approximate amount of the car purchase is **{format_salary(round(new_y_pred[0]))}$**", icon=":material/arrow_forward:")
                else:
                    st.warning("Please fill in all the fields to make a prediction.")
            except Exception as e:
                st.warning("Please fill in all the fields to make a prediction.")
        else:
            st.error("Please fill in all the fields to make a prediction.")








    # Footer
    st.markdown(
        """
        <div class='text' style="text-align: center; font-size: 16px; margin-top: 40px;">
            Created with ❤️ using Streamlit 👨‍💻 by Emre Çakır
        </div>
        """,
        unsafe_allow_html=True
    )






# ----------------- Page 2: CO2 Emissions Prediction Model -----------------
if selected == "Regression: CO2 Emissions Prediction Model":
    
    # Title 1
    st.markdown(f"<div class='title'>Welcome to CO2 Emissions Prediction Model</div>", unsafe_allow_html=True)

    # Sub-title
    st.markdown("<div class='subtitle'>A Linear Regression Model</div>", unsafe_allow_html=True)

    # Summary of the model
    st.markdown(
        """
        <div class='text'>
            The CO2 Emissions Prediction Model is a regression-based machine learning project designed to predict the CO2 
            emissions of vehicles based on various features such as engine size, fuel consumption, and transmission type. 
            This model addresses a critical environmental issue by providing insights into how different vehicle characteristics 
            impact CO2 emissions, enabling informed decision-making for manufacturers, policymakers, and consumers.
        </div>
        """,
        unsafe_allow_html=True
    )

    # import image
    ase, esa, res= st.columns([1, 3, 1])
    with esa:
        st.image("pages/dalle2.jpg", use_container_width =True)
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

    # Explanation for the model [Objective, Key Features, Machine Learning Technique]
    st.markdown(
        """
        <div class='text'>
            <strong>Objective:</strong>
            <ul>
                <li>Predict the approximate CO2 emissions of vehicles, measured in grams per kilometer, based on their specifications.</li>
            </ul>
            <strong>Key Features:</strong>
            <ul>
                <li>Engine Size (liters)</li>
                <li>Number of Cylinders</li>
                <li>Fuel Consumption Combined (L/100 km - 55% city, 45% highway)</li>
                <li>Fuel Type (Regular Gasoline, Premium Gasoline, Diesel, Ethanol)</li>
            </ul>
            <strong>Machine Learning Technique:</strong>
            <ul>
                <li>Linear Regression</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Title 2
    st.markdown(f"<div class='title'>Make Some Prediction</div>", unsafe_allow_html=True)

    x, y = st.columns([1, 1])

    # Fuel Type Selection Block
    with x:
        
        st.markdown("<div class='title-under-line'>Fuel Type Selection:</div>", unsafe_allow_html=True)

        # Create a selectbox for fuel type
        fuel_type = st.selectbox(
            label="",
            options=["Regular Gasoline", "Premium Gasoline", "Diesel", "Ethanol"],  # Options to choose from
            index=None,  # Default selected option
            help="Please select the fuel type of the vehicle",  # Help text displayed below the selectbox
            placeholder="Choose the fuel type...",  # Text displayed when no option is selected
        )
        if fuel_type == None:
            st.error("Please select the fuel type.")
        else:
            st.info(f"The fuel type selected is {fuel_type}")

    # Number of Cylinders Selection the range of from 3 to 16
    with y:
        
        st.markdown("<div class='title-under-line'>Cylinders Selection:</div>", unsafe_allow_html=True)

        # Create a selectbox for Cylinders Selection
        cylinders = st.selectbox(
            label="",
            options=list(range(3, 17)),  # Options to choose from
            index=None,  # Default selected option
            help="Please select the number of cylinders of the vehicle",  # Help text displayed below the selectbox
            placeholder="Choose the number of cylinders...",  # Text displayed when no option is selected
        )
        if cylinders == None:
            st.error("Please select the number of cylinders.")
        else:
            st.info(f"The number of cylinders selected is {cylinders}")
          
    st.write("------------")

    # Engine Size Selection
    st.markdown("<div class='title-under-line'>Engine Size Selection:</div>", unsafe_allow_html=True)

    # Engine Size slider
    engine_size = st.slider(
        label="",
        min_value=0.9,  # Minimum value
        max_value=8.5,  # Maximum value
        value=0.9,  # Default value
        step=0.1,  # Step size
        format="%.1f",  # Format of the value as a float
        help="Please select the engine size in liters",  # Help text displayed below the slider
    )

    st.info(f"The engine size selected is {engine_size} liters")
    
    st.write("------------")

    # Fuel Consumption Selection
    st.markdown("<div class='title-under-line'>Fuel Consumption Selection:</div>", unsafe_allow_html=True)

    # Fuel Consumption slider
    fuel_cons = st.slider(
        label="",
        min_value=4.0,  # Minimum value
        max_value=27.0,  # Maximum value
        value=4.0,  # Default value
        step=0.1,  # Step size
        format="%.1f",  # Format of the value as a float
        help="Please select the Fuel Consumption in L/100 km. It must be 55% city, 45% highway.",  # Help text displayed below the slider
    )

    st.info(f"The fuel consumption selected is {fuel_cons} L/100 km")

    st.write("-----------------")


    # Linear Regression Model
    import joblib
    import pandas as pd

    with open('CO2_Emissions_Canada.pkl', 'rb') as f:
        loaded_pipeline_2 = joblib.load(f)

    new_df_2 = pd.DataFrame({
        "Engine Size(L)": engine_size,
        "Cylinders": cylinders,
        "Fuel Consumption Comb (L/100 km)": fuel_cons,
        "Fuel_Type_E": 0,
        "Fuel_Type_X": 0,
        "Fuel_Type_Z": 0
    }, index=["Values"])


    st.markdown(button_style, unsafe_allow_html=True)

    if st.button("Predict CO2 Emissions"):
        try: 
            if fuel_type.lower() == "regular gasoline":
                new_df_2["Fuel_Type_X"] = 1
            elif fuel_type.lower() == "premium gasoline":
                new_df_2["Fuel_Type_Z"] = 1
            elif fuel_type.lower() == "ethanol (e85)":
                new_df_2["Fuel_Type_E"] = 1
            
            new_y_pred_2 = loaded_pipeline_2.predict(new_df_2)
            if new_y_pred_2 < 0:
                st.error("Car purchasing seems not possible according to these values above.", icon=":material/warning:")
            else:
                ff, ss = st.columns([2, 1])  # Adjust the width ratio of the columns
                with ff:
                    st.success("Prediction is made!", icon=":material/thumb_up:")

                    st.markdown(
                        f"""
                        <div class="result-box">
                        <strong>Your Inputs:</strong><br>
                        <ul>
                            <li><strong>Cylinders:</strong> {cylinders}</li>
                            <li><strong>Fuel Type:</strong> {(fuel_type)}</li>
                            <li><strong>Engine Size:</strong> {engine_size} L</li>
                            <li><strong>Fuel Consumption Comb.:</strong> {(fuel_cons)} L/100 km</li>
                            
                        </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )  

                    st.write("")

                    st.markdown(
                        f"""
                        <div class="result-box-2">
                        Estimated CO2 emissions of car:
                        <ul>
                            <h4><strong>{int(new_y_pred_2[0])} g/km</strong></h4>
                        </ul>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        except:
            st.warning("Please fill in all the fields to make a prediction.")

    # Footer
    st.markdown(
        """
        <div class='text' style="text-align: center; font-size: 16px; margin-top: 40px;">
            Created with ❤️ using Streamlit 👨‍💻 by Emre Çakır
        </div>
        """,
        unsafe_allow_html=True
    )






# ----------------- Heart Disease Prediction Model -----------------
if selected == "Classification: Heart Disease Prediction Model":
    
    # Title 1
    st.markdown(f"<div class='title'>Welcome to Heart Disease Prediction Model</div>", unsafe_allow_html=True)

    # Sub-title
    st.markdown("<div class='subtitle'>A Classification Model</div>", unsafe_allow_html=True)

    # Summary of the model
    st.markdown(
        """
        <div class='text'>
            The Heart Disease Prediction Model is a machine learning project aimed at predicting the 
            presence of heart disease in patients based on their medical attributes. This model provides 
            valuable insights that could assist healthcare professionals in identifying at-risk individuals, 
            enabling timely interventions and personalized treatment plans.
        </div>
        """,
        unsafe_allow_html=True
    )

    # import image
    xxx, zzz, ccc= st.columns([1, 3, 1])
    with zzz:
        st.image("pages/dalle3.jpg", use_container_width =True)
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

    # Explanation for the model [Objective, Key Features, Machine Learning Technique]
    st.markdown(
        """
        <div class='text'>
            <strong>Objective:</strong>
            <ul>
                <li>The objective of this project is to develop a binary classification model to accurately predict whether a patient has heart disease based on their medical data.</li>
            </ul>
            <strong>Input Features:</strong>
            <ul>
                <li><strong>Age:</strong> Age of the patient in years.</li>
                <li><strong>Gender:</strong> Gender of the patient.</li> 
                <li><strong>Chest Pain Type:</strong> Type of chest pain experienced such as Typical Angina, Atypical Angina, Non-Anginal Pain and Asymptomatic.</li> 
                <li><strong>Resting Blood Pressure:</strong> Resting blood pressure (in mm Hg) at the time of hospital admission.</li> 
                <li><strong>Cholesterol:</strong> Serum cholesterol in mg/dl.</li> 
                <li><strong>Fasting Blood Sugar:</strong> Whether fasting blood sugar level is above 120 mg/dl.</li> 
                <li><strong>Resting Electrocardiographic Results:</strong> Results of the resting ECG.</li> 
                <li><strong>Maximum Heart Rate Achieved:</strong> Maximum heart rate achieved during exercise.</li> 
                <li><strong>Exercise-Induced Angina:</strong> Whether exercise-induced chest pain occurs.</li> 
                <li><strong>ST Depression Induced by Exercise:</strong> ST depression relative to rest induced by exercise.</li> 
                <li><strong>Slope of the Peak Exercise ST Segment:</strong> ST depression relative to rest induced by exercise.</li> 
                <li><strong>Number of Major Vessels Colored by Fluoroscopy:</strong> Number of major blood vessels (0–4) colored by fluoroscopy.</li> 
                <li><strong>Thalassemia :</strong> Blood disorder (thalassemia).</li> 
            </ul>
            <strong>Target Features:</strong>
            <ul>
                <li><strong>Heart Disease:</strong> Indicates the presence or absence of heart disease.</li>
            </ul>
            <strong>Machine Learning Techniques:</strong>
            <ul>
                <li>Logistic Regression</li>
                <li>Support Vector Machines</li>
                <li>Random Forest</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Title 2
    st.markdown(f"<div class='title'>Make Some Prediction</div>", unsafe_allow_html=True)


    ooo, ttt = st.columns([2, 2])

    with ooo:
        # Gender Selection Title
        st.markdown("<div class='title-under-line'>Gender Selection:</div>", unsafe_allow_html=True)

        # Create a selectbox
        gender = st.selectbox(
            label="",
            options=["Male", "Female"],  # Options to choose from
            index=None,  # Default selected option
            help="Please select your gender",  # Help text displayed below the selectbox
            placeholder="Choose your gender...",  # Text displayed when no option is selected          
        )

        st.write("-------------")

        # Chest Pain Type Selection Title
        st.markdown("<div class='title-under-line'>Chest Pain Type Selection:</div>", unsafe_allow_html=True)

        # Create a selectbox
        cp = st.selectbox(
            label="",
            options=["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"],  # Options to choose from
            index=None,  # Default selected option
            help="Please select the Chest Pain Type",  # Help text displayed below the selectbox
            placeholder="Choose the Chest Pain Type...",  # Text displayed when no option is selected          
        )

        st.write("-------------")

        # Fasting Blood Sugar Selection Title
        st.markdown("<div class='title-under-line'>Fasting Blood Sugar Selection:</div>", unsafe_allow_html=True)

        # Create a selectbox
        fbs = st.selectbox(
            label="",
            options=["Greater than 120 mg/dl", "Less than 120 mg/dl"],  # Options to choose from
            index=None,  # Default selected option
            help="Please select the Fasting Blood Sugar",  # Help text displayed below the selectbox
            placeholder="Choose the Fasting Blood Sugar...",  # Text displayed when no option is selected          
        )

        st.write("-------------")

        # Resting Blood Pressure Selection Title
        st.markdown("<div class='title-under-line'>Resting Electro. Results Selection:</div>", unsafe_allow_html=True)

        # Create a selectbox
        restecg = st.selectbox(
            label="",
            options=["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"],  # Options to choose from
            index=None,  # Default selected option
            help="Please select the Resting Electrocardiographic Results",  # Help text displayed below the selectbox
            placeholder="Choose the Resting Electrocardiographic Results...",  # Text displayed when no option is selected          
        )


    with ttt:
        # Exercise-Induced Angina Selection Title
        st.markdown("<div class='title-under-line'>Exercise-Induced Chest Pain:</div>", unsafe_allow_html=True)

        # Create a selectbox
        exang = st.selectbox(
            label="",
            options=["Yes", "No"],  # Options to choose from
            index=None,  # Default selected option
            help="Please select the Exercise-Induced Angina",  # Help text displayed below the selectbox
            placeholder="Choose the Exercise-Induced Angina...",  # Text displayed when no option is selected          
        )

        st.write("-------------")

        # Slope of the Peak Exercise ST Segment Selection Title
        st.markdown("<div class='title-under-line'>Slope of the Peak Exercise ST:</div>", unsafe_allow_html=True)

        # Create a selectbox
        slope = st.selectbox(
            label="",
            options=["Upsloping", "Flat", "Downsloping"],  # Options to choose from
            index=None,  # Default selected option
            help="Please select the Slope of the Peak Exercise ST Segment",  # Help text displayed below the selectbox
            placeholder="Choose the Slope of the Peak Exercise ST Segment...",  # Text displayed when no option is selected          
        )

        st.write("-------------")

        # Number of Major Vessels Colored by Fluoroscopy Selection Title
        st.markdown("<div class='title-under-line'>Number of Major Vessels Colored:</div>", unsafe_allow_html=True)

        # Create a selectbox
        ca = st.selectbox(
            label="",
            options=[0, 1, 2, 3],  # Options to choose from
            index=None,  # Default selected option
            help="Please select Number of Major Vessels Colored by Fluoroscopy",  # Help text displayed below the selectbox
            placeholder="Choose an option...",  # Text displayed when no option is selected          
        )

        st.write("-------------")

        # Thalassemia Selection Title
        st.markdown("<div class='title-under-line'>Thalassemia Selection:</div>", unsafe_allow_html=True)

        # Create a selectbox
        thal = st.selectbox(
            label="",
            options=["Fixed Defect", "Normal", "Reversible Defect"],  # Options to choose from
            index=None,  # Default selected option
            help="Please select the Thalassemia: .",  # Help text displayed below the selectbox
            placeholder="Choose an option...",  # Text displayed when no option is selected          
        )

    st.write("---------")

    # Create a slide for age
    # Age Selection
    st.markdown("<div class='title-under-line'>Age Selection:</div>", unsafe_allow_html=True)

    # Age slider
    age = st.slider(
        label="",
        min_value=17,  # Minimum value
        max_value=100,  # Maximum value
        value=17,  # Default value
        step=1,  # Step size
        format="%d",  # Format of the value as an integer
        help="Please select your age",  # Help text displayed below the slider
    )

    # Create a slide for Resting Blood Pressure
    # Resting Blood Pressure Selection
    st.markdown("<div class='title-under-line'>Resting Blood Pressure Selection:</div>", unsafe_allow_html=True)

    # Resting Blood Pressure slider
    trestbps = st.slider(
        label="",
        min_value=89,  # Minimum value
        max_value=200,  # Maximum value
        value=89,  # Default value
        step=1,  # Step size
        format="%d",  # Format of the value as an integer
        help="Please select your Resting Blood Pressure",  # Help text displayed below the slider
    )

    # Create a slide for Cholesterol 
    # Cholesterol  Selection
    st.markdown("<div class='title-under-line'>Cholesterol Selection:</div>", unsafe_allow_html=True)

    # Cholesterol slider
    chol = st.slider(
        label="",
        min_value=99,  # Minimum value
        max_value=600,  # Maximum value
        value=99,  # Default value
        step=1,  # Step size
        format="%d",  # Format of the value as an integer
        help="Please select your Cholesterol ",  # Help text displayed below the slider
    )

    # Create a slide for Maximum Heart Rate Achieved 
    # Maximum Heart Rate Achieved  Selection
    st.markdown("<div class='title-under-line'>Maximum Heart Rate Achieved Selection:</div>", unsafe_allow_html=True)

    # Maximum Heart Rate Achieved slider
    thalach = st.slider(
        label="",
        min_value=59,  # Minimum value
        max_value=250,  # Maximum value
        value=59,  # Default value
        step=1,  # Step size
        format="%d",  # Format of the value as an integer
        help="Please select your Maximum Heart Rate Achieved ",  # Help text displayed below the slider
    )

    # Create a slide for ST Depression Induced by Exercise 
    # ST Depression Induced by Exercise  Selection
    st.markdown("<div class='title-under-line'>ST Depression Induced by Exercise Selection:</div>", unsafe_allow_html=True)

    # ST Depression Induced by Exercise slider
    oldpeak = st.slider(
        label="",
        min_value=-0.1,  # Minimum value
        max_value=7.0,  # Maximum value
        value=-0.1,  # Default value
        # Step size
        format="%.1f",  # Format of the value as a float
        help="Please select your ST Depression Induced by Exercise ",  # Help text displayed below the slider
    )


    # create a showcase for the selected values. If a value is not selected, specify it.
    # Showcase for the selected values in a table format
    import pandas as pd
    st.markdown("<div class='title'>Selected Values:</div>", unsafe_allow_html=True)

    def format_value(value):
        if value == "Not selected":
            return f"<span style='color:rgba(255, 82, 82, 0.65);'>{value}</span>"
        return value

    showcase_data = {
        "Gender": gender if gender else "Not selected",
        "Chest Pain Type": cp if cp else "Not selected",
        "Fasting Blood Sugar": fbs if fbs else "Not selected",
        "Resting Electrocardiographic Results": restecg if restecg else "Not selected",
        "Exercise-Induced Angina": exang if exang else "Not selected",
        "Slope of the Peak Exercise ST Segment": slope if slope else "Not selected",
        "Number of Major Vessels Colored by Fluoroscopy": ca if ca else "Not selected",
        "Thalassemia": thal if thal else "Not selected",
        "Age": age if age != 17 else "Not selected",
        "Resting Blood Pressure": trestbps if trestbps != 89 else "Not selected",
        "Cholesterol": chol if chol != 99 else "Not selected",
        "Maximum Heart Rate Achieved": thalach if thalach != 59 else "Not selected",
        "ST Depression Induced by Exercise": oldpeak if oldpeak != -0.1 else "Not selected",
    }

    # Convert the showcase data to a DataFrame for better display
    showcase_df = pd.DataFrame(list(showcase_data.items()), columns=["Feature", "Value"])

    # Apply formatting to the DataFrame
    showcase_df["Value"] = showcase_df["Value"].apply(format_value)

    # Display the DataFrame as a table with left-aligned text and emphasized column names
    st.markdown(
        showcase_df.to_html(escape=False, index=False, justify='left').replace(
            '<th>', '<th style="color:rgb(4, 182, 252); font-weight: bold; background-color:rgba(175, 175, 175, 0.31); border: 1px solid rgba(255, 255, 255, 0.88);">'
        ).replace(
            '<tr>', '<tr style="background-color:rgba(0, 0, 0, 0.61);">'
        ).replace(
            '<tr style="background-color:rgb(0, 0, 0);"><th', '<tr style="background-color:rgb(0, 0, 0);"><th'
        ).replace(
            '<td>', '<td style="padding: 8px; border: 1px solid rgba(255, 255, 255, 0.88); color: rgba(255, 255, 255, 0.88);">'
        ), 
        unsafe_allow_html=True
    )


    # convert the variables
    kk, ll = st.columns(2)
    with kk:
        # Age
        if gender == "Male":
            gender = 1
        elif gender == "Female":
            gender = 0

        # Chest Pain Type
        if cp == "Typical Angina":
            cp = 1
        elif cp == "Atypical Angina":
            cp = 2
        elif cp == "Non-Anginal Pain":
            cp = 3
        elif cp == "Asymptomatic":
            cp = 0

        # Fasting Blood Sugar
        if fbs == "Greater than 120 mg/dl":
            fbs = 1
        elif fbs == "Less than 120 mg/dl":
            fbs = 0

        # Resting Electro. Results:
        if restecg == "Normal":
            restecg = 0
        elif restecg == "ST-T wave abnormality":
            restecg = 1
        elif restecg == "Left ventricular hypertrophy":
            restecg = 2    

        # Exercise-Induced Chest Pain:
        if exang == "Yes":
            exang = 1
        elif exang == "No":
            exang = 0

        # Slope of the Peak Exercise ST Segment
        if slope == "Upsloping":
            slope = 0
        elif slope == "Flat":
            slope = 1
        elif slope == "Downsloping":
            slope = 2

        # Thalassemia 
        if thal == "Fixed Defect":
            thal = 1
        elif thal == "Normal":
            thal = 2
        elif thal == "Reversible Defect":
            thal = 3

    if age == 17:
        age = "Not selected"
    if trestbps == 89:
        trestbps = "Not selected"
    if chol == 99:
        chol = "Not selected"
    if thalach == 59:
        thalach = "Not selected"
    if oldpeak == -0.1:
        oldpeak = "Not selected"


    # create a dataframe for prediction model
    df = pd.DataFrame({
        "age": age,
        "sex": gender,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }, index=["Values"])

    import joblib

    with open('logistic_regression.pkl', 'rb') as f:
        loaded_lg = joblib.load(f)

    with open('support_vector.pkl', 'rb') as f:
        loaded_svc = joblib.load(f)

    with open('random_forest.pkl', 'rb') as f:
        loaded_rf = joblib.load(f)



    if st.button("Predict Heart Disease"):
        try: 
            my_num = 0
            for i in range(len(df.columns)):
                if df.iloc[0, i] != "Not selected":
                    my_num += 1

            if my_num == 13:
                lg_result = loaded_lg.predict(df)
                svc_result = loaded_svc.predict(df)
                rf_result = loaded_rf.predict(df)

                # st.write(lg_result)
                # st.write(svc_result)
                # st.write(rf_result)

                # Create a DataFrame to display the results
                results_df = pd.DataFrame({
                    "Model": ["Logistic Regression", "Support Vector Machine", "Random Forest"],
                    "Prediction (Heart Disease / No Heart Disease)": ["Heart Disease" if lg_result[0] == 1 else "No Heart Disease",
                                   "Heart Disease" if svc_result[0] == 1 else "No Heart Disease",
                                   "Heart Disease" if rf_result[0] == 1 else "No Heart Disease"]
                })

                # Display the results in a table
                st.markdown("<div class='title'>Prediction Results:</div>", unsafe_allow_html=True)
                st.table(results_df)

            else:
                st.warning("Please fill in all the fields to make a prediction.")


        except:
            st.warning("Please fill in all the fields to make a prediction.")





















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