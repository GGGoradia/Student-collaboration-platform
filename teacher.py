import streamlit as st
import pandas as pd

# Database to store teacher information and reviews
teacher_database = {
    "Chanthini Baskar": {
        "name": "Chanthini Baskar",
        "subject": "Microprocessors and Microcontrollers",
        "venue": "AB1 606",
        "reviews": [],
    },
    "Teacher2": {
        "name": "Teacher2",
        "subject": "Science",
        "venue": "Room 102",
        "reviews": [],
    },
}


def view_teacher_reviews():
    st.title("Teacher Reviews")
    teacher_name = st.text_input("Enter teacher's name")
    if teacher_name in teacher_database:
        teacher = teacher_database[teacher_name]
        st.write(f"Teacher Name: {teacher['name']}")
        st.write(f"Subject: {teacher['subject']}")
        st.write(f"Venue: {teacher['venue']}")

        # Display existing reviews
        if teacher['reviews']:
            st.header("Existing Reviews:")
            for review in teacher['reviews']:
                st.write(review)
            # Calculate and display the average rating
            average_rating = calculate_average_rating(teacher['reviews'])
            st.write(f"Average Rating: {average_rating:.2f}")
        else:
            st.info("No reviews available for this teacher.")
    else:
        st.warning("Teacher not found. Please enter a valid teacher name.")


def write_teacher_review():
    st.title("Write Teacher Review")
    teacher_name = st.text_input("Enter teacher's name")
    if teacher_name in teacher_database:
        teacher = teacher_database[teacher_name]
        st.write(f"Teacher Name: {teacher['name']}")
        st.write(f"Subject: {teacher['subject']}")
        st.write(f"Venue: {teacher['venue']}")

        # Add star rating input
        star_rating = st.slider("Rate the teacher (1-5)", min_value=1, max_value=5)

        # Write a review
        review_text = st.text_area("Write your review")
        if st.button("Submit Review"):
            teacher['reviews'].append(f"Rating: {star_rating} - {review_text}")
            st.success("Review submitted successfully.")
    else:
        st.warning("Teacher not found. Please enter a valid teacher name.")


def calculate_average_rating(reviews):
    total_ratings = 0
    for review in reviews:
        rating = int(review.split('-')[0].strip().split()[-1])
        total_ratings += rating
    if len(reviews) > 0:
        return total_ratings / len(reviews)
    else:
        return 0.0


# Run the app
if __name__ == "__main__":
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("View Teacher Reviews", "Write Teacher Review"))

    if page == "View Teacher Reviews":
        view_teacher_reviews()
    else:
        write_teacher_review()