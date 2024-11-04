import streamlit as st
from PIL import Image

# Define paths to images in the same directory (adjust if your images are in a subdirectory)
screen_paths = {
    "Login Screen": "Login Screen.png",
    "Dashboard": "Dashboard.png",
    "Project Card Creation": "Project Card Creation.png",
    "Project Details Page": "Project Details Page.png",
    "Resource Matching Suggestions": "Resourse Matching Suggestions.png",
    "Review and Submit": "Review and Submit.png",
    "Confirmation": "Confirmation.png",
}

# Navigation flow in the sequence of screens
navigation_flow = [
    "Login Screen",
    "Dashboard",
    "Project Card Creation",
    "Project Details Page",
    "Resource Matching Suggestions",
    "Review and Submit",
    "Confirmation"
]

# Initialize session state to keep track of the current screen index
if "screen_index" not in st.session_state:
    st.session_state.screen_index = 0

# Display the current screen image
current_screen = navigation_flow[st.session_state.screen_index]
st.image(Image.open(screen_paths[current_screen]), caption=current_screen, use_column_width=True)

# Navigation buttons
col1, col2 = st.columns([1, 1])
if col1.button("Previous") and st.session_state.screen_index > 0:
    st.session_state.screen_index -= 1
if col2.button("Next") and st.session_state.screen_index < len(navigation_flow) - 1:
    st.session_state.screen_index += 1
