
# find_and_download_file.py
import streamlit as st
from pymongo import MongoClient
from gridfs import GridFS

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["file_storage_db"]
grid = GridFS(db, "files")


def find_file():
    st.title("Find and Download PDF/PPT File from MongoDB")

    # Get user inputs for file details
    filename = st.text_input("Enter File Name:")

    if st.button("Find and Download File"):
        download_file(filename)


def download_file(filename):
    file = grid.find_one({"filename": filename})

    if file:
        st.subheader(f"File: {filename}")
        file_data = file.read()

        # Offer a download button for the file
        st.download_button(
            label="Download File",
            data=file_data,
            key=filename,
        file_name = filename,
        )
    else:
        st.error("File not found.")


if __name__ == "__main__":
    find_file()
