import streamlit as st
import requests
from streamlit_lottie import st_lottie
from pathlib import Path
import json

current_dir = Path(__file__).parent

# Favicon
st.set_page_config(page_title="Techno Clear", page_icon=str(current_dir / "images" / "logo" / "clear_logo.png"), layout="centered")

# Use local CSS
def local_css(file_name):
    # Get the absolute path to the current directory where app.py is located
    current_dir = Path(__file__).parent

    # Construct the path to the css file based on the current directory
    css_path = current_dir / file_name

    with css_path.open() as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns([1,6])
    with left_column:
        st.image(str(current_dir / "images" / "logo" / "clear_logo.png"))
    with right_column:
        st.title("Techno Clear")
        
    st.subheader("Transforming Hours into Seconds") 
    st.write("Smart Apps for Efficient Business Automation")
    st.write("##")










# ---- WHAT WE DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("""
        **Techno Clear: Your Automation Specialist**

        - **Build**: We craft applications tailored to your company's specific needs.
        - **Maintain**: Continuous support ensures your processes run smoothly.
        - **Personalization**: Your company is unique. So is the solution we provide.
        """)

    with right_column:
        def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)
        lottie_trading = load_lottiefile(str(current_dir / "images" / "company_lottie.json"))
        st_lottie(lottie_trading, speed=1, height=200)


    st.write("""
        **Speed Up Your Business**:
        You take days to create reports, design dashboards, format data and spreadsheets, contact customers and more ?
        
        **With Techno Clear, it's just a second with a press of the 'Run' button.**
        """)
    






# ---- BACKTRADER ----
with st.container():
    st.write("---")
    st.header("Our Projects")
    st.write("##")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(str(current_dir / "images" / "people_svg" / "4.svg"))

    with text_column:
        st.subheader("Backtest your trading strategies")
        st.write(
            """
            Want to validate and refine your trading strategy? 
            
            Use our app to backtest your trading strategy efficiently, optimize for better returns and visualize the results for clear analysis.
            """
        )
        st.markdown("[Visit our Backtester...](https://backtester-g9xl.onrender.com/)")



# ---- SPREADSHEET ----
with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(str(current_dir / "images" / "people_svg" / "3.svg"))

    with text_column:
        st.subheader("Advanced Spreadsheet Processor")
        st.write(
            """
            Transform raw data into actionable insights.

            Import and process data effortlessly with our application. Extract key information and receive tailored output files. Get structured, ready-to-use datasets in just a click.
            """
        )
        #st.markdown("[Watch Video...](https://youtu.be/123)")



# ---- ACCOUNTING ----
with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(str(current_dir / "images" / "people_svg" / "2.svg"))

    with text_column:
        st.subheader("Streamline Invoice Management")
        st.write(
            """
            Invoicing taking up too much time?

            Introducing an automation app that scans, categorizes, and manages invoices. Say goodbye to manual data entry and errors.
            """
        )
        #st.markdown("[Try AutoInvoice...](https://autoinvoice-g9xl.onrender.com/)")




# ---- EDUCATION ----
with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(str(current_dir / "images" / "people_svg" / "1.svg"))

    with text_column:
        st.subheader("Assignment Organizer for Educators")
        st.write(
            """
            Streamline student homework and assignments.

            Our app helps educators to distribute, collect, and organize assignments in one place. Simplifying the grading process and making class management seamless.
            """
        )
       #st.markdown("[Use TeachEase...](https://teachease-g9xl.onrender.com/)")




# ---- RESTAURANT ROSTERING ----
with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(str(current_dir / "images" / "people_svg" / "5.svg"))

    with text_column:
        st.subheader("Automated Roster Builder for Restaurants")
        st.write(
            """
            Simplify workforce scheduling for your restaurant chain.

            Our app takes into consideration staff availability, peak hours, and roles to automatically generate optimal rosters for each outlet. Ensure smooth operations with balanced work shifts.
            """
        )
        #st.markdown("[Try RosterChef...](https://rosterchef-g9xl.onrender.com/)")







# ---- CONTACT ----
with st.container():
    st.write("---")

    left_column, right_column = st.columns([2,1])
    with left_column:
        st.header("Get In Touch With Us!")
        st.write("""
        Whether you have a question, a proposal, or just want to say hello, 
        I'd love to hear from you. Don't hesitate to reach out!
        """)

        # Displaying contact options
        st.write("📧 Email: [alexandre.kocev@gmail.com](mailto:alexandre.kocev@gmail.com)")
        st.write("📞 Phone: +33 (0)6 04 43 69 84")
        st.write("🌐 Location: 69001 Lyon, France")

    with right_column:
        st.empty()




# ---- FOOTER ----
footer="""<style>
.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #f1f1f1;
  text-align: center;
  padding: 10px;
  font-size: 12px;   /* Adjust size as needed */
}
</style>

<div class="footer">
  © 2023 Techno Clear. All Rights Reserved. SIREN: 952 266 641.
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
