from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Arraj2611"
PAGE_ICON = "profile-pic.png"
NAME = "Rajeev Aken"
DESCRIPTION = """
Passionate intern with a deep interest in AI/ML, and Computer Vision. Proficient in Python, Java, and various languages. Eager to apply theoretical knowledge in a hands-on internship, contributing to innovative projects and learning from experienced professionals.
"""
EMAIL = "arrajeevaken2611@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/rajeevaken/",
    "GitHub": "https://github.com/Arraj2611",
    "X": "https://x.com/AkenRajeev",
}
PROJECTS = {
    "🐶 Dog Breed Classification using MobileNetV2": "https://github.com/Arraj2611/ml_projects/blob/main/dog_breed_identification.ipynb",
    "🩺 Medical Insurance charges prediction using Neural Networks": "https://github.com/Arraj2611/ml_projects/blob/main/neural_network_Regression.ipynb",
    "👚 Classification of Fashion-MNIST dataset using Neural Networks": "https://github.com/Arraj2611/ml_projects/blob/main/NN_classification.ipynb",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ SIH 2023: Participant - Developed Sentiment Analysis of Incoming calls on a Helpdesk using ML/DL
- ✔️ Strong hands on experience and knowledge in Python
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy), SQL, Java, JavaScript, C, C++
- 📊 Data Visulization: Matplotlib, MS Excel, Plotly, Seaborn
- 📚 Modeling: Logistic regression, linear regression, decition trees, TensorFlow, Keras
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Education")
st.write("---")

# --- JOB 1
st.write("🚧", "**B.Tech | Walchand Institute of Technology**")
st.write("10/2021 - Present")
st.write(
    """
- ► CGPA till 6th semester 8.88
- ► Learnt technologies like Python, Java, Javascript, C++ etc
- ► Studied Engineering topics like Computer Architecture, Embedded Systems, Software engineering, DBMS etc
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Junior College | Walchand College of Arts and Science**")
st.write("06/2019 - 08/2021")
st.write(
    """
- ► Passed out with Distinction (89.2%)
- ► Learned basics of Science in physics, chemistry, Maths
- ► Prepared for high-level examinations like JEE mains, Advance
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
