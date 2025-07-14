import streamlit as st
import os
from reddit_scraper import scrape_user_data
from persona_generator import generate_persona
from utils import extract_username, save_persona_to_file

st.set_page_config(page_title="Reddit Persona Generator", layout="centered")

st.title("Reddit Persona Generator")

st.caption("Generate a structured user persona using Google Gemini API and Reddit data.")

input_value = st.text_input("Enter Reddit Username or Profile URL", placeholder="e.g. https://www.reddit.com/user/kojied/")

if st.button("Generate Persona"):
    if not input_value:
        st.error("Please enter a valid Reddit username or URL.")
    else:
        username = extract_username(input_value)

        with st.spinner(f"Scraping Reddit user u/{username}..."):
            data = scrape_user_data(username)

        if not data["posts"] and not data["comments"]:
            st.error("No usable data found for this user.")
        else:
            with st.spinner("Generating persona with Gemini..."):
                persona = generate_persona(username, data)

            save_persona_to_file(username, persona)

            st.success("Persona generated!")
            st.subheader("User Persona")
            st.text_area("Output", value=persona, height=500)

            st.download_button(
                label="📄 Download Persona",
                data=persona,
                file_name=f"{username}_persona.txt",
                mime="text/plain"
            )
