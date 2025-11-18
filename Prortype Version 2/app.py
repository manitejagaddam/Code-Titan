import streamlit as st
from streamlit_extras.card import card
import pandas as pd

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------- CUSTOM CSS ----------------------
def load_css():
    st.markdown("""
        <style>
        /* Remove Streamlit default padding */
        .block-container { padding-top: 2rem; padding-bottom: 2rem; }

        /* Card Styling */
        .modern-card {
            padding: 25px;
            border-radius: 18px;
            background: #111827;
            border: 1px solid #1f2937;
            box-shadow: 0 4px 10px rgba(0,0,0,0.4);
            color: white;
        }

        /* Metric Styling */
        .metric-card {
            padding: 20px;
            border-radius: 16px;
            background: #1f2937;
            color: white;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }

        /* Buttons */
        .stButton>button {
            border-radius: 12px;
            padding: 8px 16px;
            background: #4f46e5;
            color: white;
            border: none;
            font-weight: bold;
        }
        .stButton>button:hover {
            background: #6366f1;
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #111827;
        }
        </style>
    """, unsafe_allow_html=True)


load_css()

# ---------------------- SIDEBAR NAV ----------------------
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go to:",
    ["Dashboard", "Analytics", "Settings"]
)

st.sidebar.markdown("---")
st.sidebar.write("Built with ❤️ using Streamlit")


# ---------------------- DASHBOARD PAGE ----------------------
if page == "Dashboard":
    st.title("🚀 Modern Streamlit Dashboard")
    st.write("A clean and premium UI template.")

    # Metrics Row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="metric-card"><h3>1,204</h3><p>Active Users</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-card"><h3>87%</h3><p>Model Accuracy</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="metric-card"><h3>312</h3><p>Daily Records</p></div>', unsafe_allow_html=True)

    st.markdown("### 📈 Quick Overview")

    colA, colB = st.columns(2)

    with colA:
        st.markdown("<div class='modern-card'><h4>User Insights</h4><p>This card shows a summary of insights with a modern card UI.</p></div>", unsafe_allow_html=True)

    with colB:
        st.markdown("<div class='modern-card'><h4>Performance</h4><p>Display your charts or ML outputs here.</p></div>", unsafe_allow_html=True)


# ---------------------- ANALYTICS PAGE ----------------------
elif page == "Analytics":
    st.title("📊 Analytics")

    df = pd.DataFrame({
        "Users": [100, 200, 300, 400],
        "Engagement": [20, 40, 50, 70]
    })

    st.line_chart(df)


# ---------------------- SETTINGS PAGE ----------------------
elif page == "Settings":
    st.title("⚙️ Settings")
    st.write("Configure your dashboard preferences here.")
    st.text_input("Enter your app name:", "My Streamlit App")
    st.button("Save Settings")
