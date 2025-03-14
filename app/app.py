import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from components.aqi_fetcher import get_air_quality
from components.chatbot import ask_bot
import plotly.graph_objects as go
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="Sofia Air Quality", layout="centered")

# Sidebar Navigation with clickable buttons
st.sidebar.title("🔎 Navigation")

if "page" not in st.session_state:
    st.session_state.page = "Dashboard" 

if st.sidebar.button("📊 Air Quality Dashboard"):
    st.session_state.page = "Dashboard"

if st.sidebar.button("🤖 AI Chat Assistant"):
    st.session_state.page = "Chatbot"

# Opens first page
if st.session_state.page == "Dashboard":
    st.title("🌍 Sofia Air Quality")
    
    # Fetch AQI data
    data = get_air_quality()

    if "error" in data:
        st.error(data["error"])
    else:
        st.subheader(f"📍 Air Quality in {data['city']}")

        col1, col2, col3 = st.columns(3)
        col1.metric("🌿 AQI", data["aqi"])
        col2.metric("🌡 Temperature (°C)", data["temperature"])
        col3.metric("💨 Wind Speed (m/s)", data["wind"])

        col4, col5 = st.columns(2)
        col4.metric("🫁 PM10 Level", data["pm10"])
        col5.metric("🫁 PM2.5 Level", data["pm25"] if data["pm25"] != "N/A" else "No Data")

        # Convert forecast data to lists
        pm10_days = [day["day"] for day in data["forecast_pm10"]]
        pm10_values = [day["avg"] for day in data["forecast_pm10"]]
        pm25_values = [day["avg"] for day in data["forecast_pm25"]]

    st.subheader("📊 Air Pollution Forecast")
    
    fig = px.line(
        x=pm10_days, 
        y=[pm10_values, pm25_values], 
        labels={"x": "Date", "y": "Pollutant Level"},
        title="PM10 & PM2.5 Forecast (Next 5 Days)",
        markers=True
    )

    # Customize the legend
    fig.update_traces(mode="lines+markers")
    fig.update_layout(
        xaxis_tickangle=-45,
        legend_title_text="Pollutants",
        legend=dict(x=1, y=1),  # Move legend to top-left
    )

    st.plotly_chart(fig, use_container_width=True)
    
    with st.expander("ℹ️ See more information"):
        st.subheader("🫁 Understanding PM10 & PM2.5")
        st.info("""
        - **PM10** refers to large particles (e.g., dust, pollen, mold) that can cause throat and nose irritation.
        - **PM2.5** are fine particles (from car emissions, industrial pollution) that **can enter the lungs** and affect breathing.
        - **How to reduce exposure?** 
            - 🚶 Walk in parks with more trees.
            - 🏠 Keep windows closed on high AQI days.
            - 😷 Wear a mask if pollution is high.
        """)
        # 📌 Add easy-to-understand AQI information
    
    st.subheader("🌡 Air Quality Index Gauge")

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=data["aqi"],
        title={"text": "Air Quality Index (AQI)"},
        gauge={
            "axis": {"range": [0, 300]},  # Adjust based on AQI scale
            "steps": [
                {"range": [0, 50], "color": "green"},
                {"range": [51, 100], "color": "yellow"},
                {"range": [101, 150], "color": "orange"},
                {"range": [151, 200], "color": "red"},
                {"range": [201, 300], "color": "purple"}
            ],
            "threshold": {
                "line": {"color": "red", "width": 4},
                "thickness": 0.75,
                "value": data["aqi"]
            }
        }
    ))

    st.plotly_chart(fig_gauge)
    
    with st.expander("ℹ️ See more information"):
        # 📌 Add easy-to-understand AQI information
        st.markdown("### 🧐 What does AQI mean?")
        st.info("""
        - **AQI (Air Quality Index)** measures how clean or polluted the air is.
        - The higher the AQI, the worse the air quality.
        - Air pollution can cause breathing issues, especially for children, older adults, and people with asthma.
        """)

        # 🟢 AQI Health Effects Table
        st.markdown("### 🚦 AQI Health Effects & Actions")
        st.write("""
        | AQI Level | Health Concern | Recommended Actions |
        |-----------|---------------|---------------------|
        | 🟢 **0-50 (Good)** | Air quality is good & safe | No action needed ✅ |
        | 🟡 **51-100 (Moderate)** | Air is acceptable, but some pollutants might be a concern | Sensitive people should avoid prolonged outdoor activities 🤧 |
        | 🟠 **101-150 (Unhealthy for Sensitive Groups)** | Older adults & kids should limit outdoor activities | Reduce outdoor activities, wear a mask 😷 |
        | 🔴 **151-200 (Unhealthy)** | Health effects may be felt by everyone | Avoid outdoor exercise, stay indoors 🚷 |
        | 🟣 **201-300 (Very Unhealthy)** | Health warnings for all individuals | Everyone should stay indoors, wear a mask 😷 |
        """)
     

    st.subheader("🌍 Real-Time Air Quality Map")

    # Create a map centered on Sofia
    m = folium.Map(location=[42.6977, 23.3242], zoom_start=12)

    # Add an AQI marker
    folium.Marker(
        [42.6977, 23.3242], 
        popup=f"AQI: {data['aqi']}",
        tooltip="Sofia Air Quality",
        icon=folium.Icon(color="red" if data["aqi"] > 100 else "green"),
    ).add_to(m)

    # Display the map
    folium_static(m)
    

if st.session_state.page == "Chatbot":
    st.title("🤖 Air Quality AI Chatbot")
    st.write("💬 **Ask me anything about air quality, pollution, and how to protect your health!**")
    
    st.info("""
        **Try asking:**
        - "_What does AQI mean?_"
        - "_How can I reduce my exposure to air pollution?_"
        - "_Why is PM2.5 dangerous?_"
        - "_What should I do on a high pollution day?_"
    """)

    user_input = st.text_input("Type your question here:")

    if st.button("Ask 🤖"):
        if user_input.strip():
            response = ask_bot(user_input)
            st.subheader("🤖 Response:")
            st.write(response)
        else:
            st.warning("⚠️ Please enter a valid question.")
