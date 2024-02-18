import streamlit as st
from modules.upload import upload_files
from modules.find import find_file
from modules.teacher import view_teacher_reviews, write_teacher_review

st.set_page_config(page_title="Study Material Sharing", layout="wide")

# Define navigation (excluding "Login" and "Register")
pages = {
    "Upload": upload_files,
    "Find": find_file,
    "Teacher Reviews": view_teacher_reviews,
    "Write Review": write_teacher_review,
}

st.sidebar.title("Navigation")

# Set a default page if none is selected
default_page = "Upload"

# Get the index of the default_page in the keys of the pages dictionary
default_page_index = list(pages.keys()).index(default_page)

# Allow users to select the page
page = st.sidebar.radio("Go to", tuple(pages.keys()), index=default_page_index)
pages[page]()