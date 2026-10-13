import streamlit as st
import pandas as pd
from modules.creator_studio.creator_studio import show_creator_studio

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Prismatch",
    page_icon="✨",
    layout="wide"
)

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page", ["Dashboard", "Creator Studio", "Smart Brief Builder"])

# ---------------------------------------------------------
# APPLICATION HEADER
# ---------------------------------------------------------
st.title("✨ Prismatch")
st.subheader("AI-Native Creator Marketplace")

st.write(
    "Helping brands discover creators who match their campaign goals, "
    "creative style, and budget."
)

st.markdown("---")

# ---------------------------------------------------------
# PAGE ROUTING
# ---------------------------------------------------------
if page == "Dashboard":
    st.header("📊 Marketplace Dashboard")
    st.write("Welcome to Prismatch! Use the navigation sidebar to explore the Creator Studio or Smart Brief Builder.")
    
elif page == "Creator Studio":
    # Safely call creator studio
    show_creator_studio()

elif page == "Smart Brief Builder":
    st.header("📋 Smart Brand Brief Builder")
    st.write("Create and broadcast campaign briefs to verified AI creators.")
    with st.form("brief_builder_form"):
        st.text_input("Campaign Name", "AI Commercial Video Launch")
        st.selectbox("Content Type", ["Video", "Animation", "Graphics"])
        st.form_submit_button("Submit Brief")