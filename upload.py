# upload_file.py
import streamlit as st
from pymongo import MongoClient
from gridfs import GridFS

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["file_storage_db"]
grid = GridFS(db, "files")

def upload_files():
    st.title("Upload PDF/PPT File to MongoDB")

    # Get user inputs for file details
    filename = st.text_input("Enter File Name:")
    uploaded_file = st.file_uploader("Upload a PDF/PPT file:", type=["pdf", "pptx"])

    if uploaded_file is not None:
        # Store the uploaded file in MongoDB GridFS with metadata
        file_id = grid.put(uploaded_file, filename=filename)
        st.write(f"File '{filename}' (ID: {file_id}) uploaded successfully.")

if __name__ == "__main__":
    upload_files()
