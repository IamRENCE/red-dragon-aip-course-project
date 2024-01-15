# Import key libraries and packages
import streamlit as st
import requests

st.set_page_config(page_title="Terence's AI Query Bot")
st.title("AIP Course Submission")


def header():
    st.header("Welcome to Terence's AI Query Bot")
    st.subheader("Compose a query bot response")


def submit_form():
    with st.form("submit_form", clear_on_submit=False):
        query = st.text_input("Query to submit")
        submit = st.form_submit_button("Submit")
        if submit:
            res = requests.post(
                f"http://fast_api_backend:7860/send?query={query}")
            if res.status_code == 200:
                st.markdown(f''':robot_face: {res.json()["message"]}''')
            else:
                st.markdown(f"There was an error: {res.json()['message']}")


if __name__ == "__main__":
    header()
    submit_form()
