import streamlit as st
from agents.frontend import get_frontend_part
from agents.styling import get_css_part
from agents.logic import get_logic_part
import os
import webbrowser


# ----------------- FILE GENERATION FUNCTIONS -----------------
def write_to_file_in_path(folder_path, filename, content):
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content + '\n')
    print(f"Content added to {file_path}.")

def open_file():
    file_path = os.path.abspath("sandbox/index.html")
    file_url = f"file://{file_path}"
    webbrowser.open(file_url)

def createApp(ApplicationName):
    frontend = get_frontend_part(ApplicationName)
    styling = get_css_part(ApplicationName, frontend=frontend)
    logic = get_logic_part(ApplicationName, frontend=frontend)

    folder_path = "sandbox"

    write_to_file_in_path(folder_path, "index.html", frontend)
    write_to_file_in_path(folder_path, "style.css", styling)
    write_to_file_in_path(folder_path, "app.js", logic)

    open_file()


# ----------------- PREMIUM CUSTOM CSS -----------------
def load_custom_streamlit_css():
    st.markdown("""
        <style>

        /* ----------- GLOBAL BACKGROUND ANIMATION ----------- */
        body {
            background: linear-gradient(135deg, #0f172a, #1e1b4b, #312e81);
            background-size: 400% 400%;
            animation: gradientBG 14s ease infinite;
            color: white;
        }
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Center all content */
        .main {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* Fade-in animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 {
            animation: fadeIn 0.8s ease forwards;
            margin-bottom: 5px;
            font-size: 42px !important;
        }

        /* Sub-heading text */
        .subtext {
            animation: fadeIn 1.1s ease forwards;
            color: #CBD5E1;
            font-size: 18px;
            margin-bottom: 25px;
            text-align: center;
        }

        /* ----------- CARD DESIGN ----------- */
        .app-card {
            background: rgba(30, 41, 59, 0.8);
            backdrop-filter: blur(12px);
            padding: 35px;
            border-radius: 22px;
            max-width: 520px;
            width: 95%;
            animation: fadeIn 1.3s ease forwards;

            border: 1px solid rgba(99,102,241,0.3);
            box-shadow:
                0 0 18px rgba(99,102,241,0.25),
                0 0 25px rgba(139,92,246,0.15);
            transition: 0.3s ease;
        }

        .app-card:hover {
            transform: scale(1.015);
            box-shadow:
                0 0 25px rgba(99,102,241,0.45),
                0 0 40px rgba(139,92,246,0.25);
        }

        /* ----------- INPUT FIELD ----------- */
        .stTextInput>div>div>input {
            background: #0f172a;
            color: white;
            border-radius: 12px;
            border: 1px solid #475569;
            padding: 12px;
            font-size: 16px;
            transition: 0.3s ease;
        }

        .stTextInput>div>div>input:focus {
            border: 1px solid #818CF8 !important;
            box-shadow: 0 0 10px rgba(129,140,248,0.5);
        }

        /* ----------- BUTTON ----------- */
        .stButton>button {
            background: linear-gradient(135deg, #4f46e5, #6d28d9, #7c3aed);
            background-size: 400% 400%;
            animation: buttonGradient 6s ease infinite;

            color: white;
            border-radius: 14px;
            padding: 12px 20px;
            font-weight: 600;
            font-size: 17px;
            width: 100%;
            border: none;

            transition: transform 0.15s ease, box-shadow 0.2s ease;
        }

        @keyframes buttonGradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .stButton>button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(139,92,246,0.4);
        }

        .stButton>button:active {
            transform: scale(0.96);
        }

        </style>
    """, unsafe_allow_html=True)


# ----------------- STREAMLIT UI -----------------
def main():
    st.set_page_config(page_title="CodeTitan App Generator", page_icon="⚡", layout="centered")
    load_custom_streamlit_css()

    st.markdown("<h1>⚡ CodeTitan App Generator</h1>", unsafe_allow_html=True)
    st.markdown("<div class='subtext'>Build full HTML / CSS / JS applications instantly with AI.</div>", unsafe_allow_html=True)

    # Card container
    st.markdown("<div class='app-card'>", unsafe_allow_html=True)

    app_name = st.text_input("Application Name", "")

    if st.button("Generate App"):
        if app_name.strip():
            createApp(app_name)
            st.success(f"Application '{app_name}' created successfully! 🚀")
        else:
            st.warning("Please enter a valid application name.")

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
