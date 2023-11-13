import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="Animal Recognition",
    page_icon="🐄",
    layout='wide',
)
st.title = ("Animal Recognition")
st.sidebar.success("Select a page above")


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"



# --- GENERAL SETTINGS ---
PAGE_TITLE = "Team Eco Watch"
PAGE_ICON = ":wave:"
NAME = "Eco Watch"
DESCRIPTION = """
Crop Protection System Developed by Team Eco Watch
"""



# st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# # with col2:
#     st.title(NAME)
#     st.write(DESCRIPTION)
#     st.download_button(
#         label=" 📄 Download Resume",
#         data=PDFbyte,
#         # file_name=resume_file.name,
#         mime="application/octet-stream",
#     )
#     st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
# st.write('\n')
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]({link})")

# --- About our Project ---
st.write('\n')
st.subheader("About Our Project")
st.write(
    """
-  CROP PROTECTION AND PREVALENCE SYSTEM 
FROM STRAY ANIMALS IN AMRELI DISTRICT
"""
)
# --- Aim of Our Project ---
st.write('\n')
st.subheader("Aim of Our Project")
st.write(
    """
-  In order to protect the farm from potential threats such as intruders, vermin, and UV sound-emitting scarecrows,
    establish an automated defense system that relies on sensors for movement detection and cameras for
    image detection to trigger specific deterrents.

"""
)


# --- Solution ---
st.write('\n')
st.subheader("Our Solution")
st.write(
    """
Implementing Integrated Sensors at a certain altitude along the field perimeter to identify the movement of sizable animals. Subsequently, employ the Sprinkler System to avert their approach
"""
)


# --- Team Members and Role ---
st.write('\n')
st.subheader("Team Members Name and Role:")
st.write(
    """
-  Zalak Kansagra - Faculty Mentor
-  Maitry Savaliya - Team Leader
- Harsh Vaidya - Software Developer
- Jiten Advani - Hardware Developer
- Maharshi Desai - Hardware Developer
- Devanshi Mufti - Software Developer
- Komal Mandowara - Software Developer
- Khushi Agarwal - Software Developer
- Aarjav Jani - Web Developer
"""
)