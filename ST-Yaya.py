import streamlit as st

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 100px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

pages = {
    "": [
        st.Page("./pages/home.py", title="🏠 Home")
    ],
    "🖼️ Memory of Rama Yaya": [
        st.Page("./pages/raya1.py", title="1️⃣ Album 1"),
        st.Page("./pages/raya2.py", title="2️⃣ Album 2"),
        st.Page("./pages/raya3.py", title="3️⃣ Album 3"),
        st.Page("./pages/yaya-letter.py", title="💌 Yaya's Letter")
    ],
    "Surprise for Yaya": [
        st.Page("./pages/misteri.py", title="❓ ???"),
    ],
}

pg2 = st.navigation(pages)
pg2.run()