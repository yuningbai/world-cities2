import streamlit as st

st.set_page_config(
    page_title="World Cities",
    page_icon="🌍",
    layout="wide",
)

st.title("🌍 World Cities Explorer")

st.write(
    """
    Welcome to the World Cities Explorer application!
    
    This app helps you explore and discover information about cities around the world.
    Navigate to the different sections using the sidebar to get started.
    """
)

st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Get Started")
    st.write(
        """
        Click the button to explore cities and their data.
        """
    )

with col2:
    if st.button("🚀 Go to App", key="main_button", use_container_width=True):
        st.switch_page("pages/app.py")

st.divider()

st.subheader("Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("🔍 **Search** - Find cities by name or region")

with col2:
    st.info("📊 **Analyze** - View detailed city statistics")

with col3:
    st.info("🗺️ **Explore** - Discover cities worldwide")
