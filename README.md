# 🌍 Air Quality Dashboard

## 📌 Overview
The **Sofia Air Quality Dashboard** is an experimental project as a **real-time air quality monitoring app** for **Sofia, Bulgaria**. It provides **live air pollution data, forecasts, and insights** using **interactive visualizations** and an **AI-powered chatbot** to help users understand air pollution and its health effects.

![Image](https://github.com/user-attachments/assets/ef1d671a-7795-45ce-8129-b805670790d5)

---

## 📊 **Features**
- **📍 Real-time AQI Data** - Displays **AQI, temperature, wind speed, PM10, and PM2.5 levels** for Sofia.
- **📈 Forecast Trends** - 5-day **pollution level forecast** with interactive charts.
- **🗺️ Interactive Air Quality Map** - Shows **real-time AQI level** for the specified location in Sofia.
- **🤖 AI Chat Assistant** - Ask the chatbot **questions about air pollution, health effects, and preventive measures**.
- **🚦 AQI Health Guidelines** - Explains **AQI levels and recommended actions**.

---

## ⚙️ **Tech Stack**
- **🖥️ Frontend:** [Streamlit](https://streamlit.io/)
- **📡 API Source:** [World Air Quality Index API](https://waqi.info/)
- **📊 Visualization:** Matplotlib, Plotly, Folium
- **🤖 AI Model:** LLaMA-based chatbot (via `llama-cpp-python`)

---

## 🛠 **Setup & Installation**
### **1️⃣ Clone the Repository**
```bash
  git clone https://github.com/your-username/your-repository-name.git
  cd your-repository-name
```

### **2️⃣ Create a Virtual Environment**
```
python -m venv env
source env/bin/activate   # For MacOS/Linux
env\Scripts\activate.bat      # For Windows
```

### **3️⃣ Install Dependencies**
```pip install -r requirements.txt```

### **4️⃣ Add Your API Key**

    Get an API key from WAQI API.
    Store it in .env file (create it in the root directory).

```API_KEY=your-api-key-here```

### **5️⃣ Run the Application**

```streamlit run app.py```

