import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from pathlib import Path
import json
# to convert from svg to png
import cairosvg
from PIL import Image
from io import BytesIO

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


# Display svg images
def svg_to_pil_image(svg_path):
    """Convert svg file to a transparent background PIL Image."""
    # Convert SVG to PNG with transparent background
    output = BytesIO()
    with open(svg_path, "rb") as f:
        cairosvg.svg2png(file_obj=f, write_to=output)
    
    # Open the PNG image with PIL
    image = Image.open(output)
    
    # Ensure the image has an alpha channel for transparency
    image = image.convert("RGBA")
    
    # Get data of the image
    datas = image.getdata()
    
    # Create a new image data list
    new_data = []
    
    # Loop through the image data
    # If the pixel is white (or close to white), make it transparent
    # Otherwise, keep the original pixel
    for item in datas:
        if item[0] > 220 and item[1] > 220 and item[2] > 220:  # Change these values if needed
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    
    # Update image data
    image.putdata(new_data)
    return image









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
        You take days to create reports, design dashboards, contact customers, and more ?
        
        **With Techno Clear, it's just a second with a press of the 'Run' button.**
        """)
    






# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Our Projects")
    st.write("##")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(svg_to_pil_image(str(current_dir / "images" / "people_svg" / "2.svg")))

        #st.image(Image.open("images/people/2.png"))
    with text_column:
        st.subheader("Backtest your trading strategies")
        st.write(
            """
            Want to validate and refine your trading strategy? Our app can:
            - **backtest** your trading strategy efficiently.
            - **optimize** and fine-tune for best results.
            - **visualize** and plot the results for clear analysis.
            
            Dive in and make your trading strategy more robust.
            """
        )
        st.markdown("[Visit our Backtester...](https://backtester-g9xl.onrender.com/)")


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(svg_to_pil_image(str(current_dir / "images" / "people_svg" / "1.svg")))
        #st.image(Image.open("images/people/1.png"))
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/123)")




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
