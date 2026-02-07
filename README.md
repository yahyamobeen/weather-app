# **🌦️ FastAPI Weather App**

A full-stack weather application built with **FastAPI** that fetches real-time temperature data for cities worldwide. This project demonstrates backend API development, third-party API integration, and serving a static frontend using Python.

[**🔴 Live Demo**](https://weather-app-sp82.onrender.com/static/)

## **🚀 Features**

* **Real-Time Weather:** Fetches live data from the [WeatherAPI](https://www.weatherapi.com/) service.  
* **Robust Backend:** Built with **FastAPI** for high performance and automatic documentation.  
* **Strict Typing:** Uses **Pydantic** models to validate incoming requests and outgoing responses.  
* **Synchronous Integration:** Utilizes the requests library for external API calls.  
* **Static Frontend:** Serves HTML, CSS, and JavaScript directly from the FastAPI server.  
* **CORS Support:** Configured to handle Cross-Origin Resource Sharing for secure communication.

## **🛠️ Tech Stack**

* **Framework:** FastAPI  
* **Server:** Uvicorn  
* **Language:** Python 3  
* **API Integration:** Requests module  
* **Validation:** Pydantic  
* **Frontend:** HTML5, CSS3, Vanilla JavaScript  
* **Deployment:** Render

## **📂 Project Structure**

.  
├── app/  
│   ├── weather/  
│   │   └── weather.py       \# API Router logic  
│   └── schemas\_weather.py   \# Pydantic data models  
├── frontend/  
│   ├── index.html           \# User Interface  
│   ├── style.css            \# Styling  
│   └── script.js            \# Frontend logic (Fetch API)  
├── main\_weather.py          \# Application entry point  
├── requirements.txt         \# Dependencies  
└── .env                     \# Environment variables (Not uploaded)

## **⚡ Installation & Setup**

Follow these steps to run the project locally on your machine.

### **1\. Clone the Repository**

git clone \[https://github.com/yahyamobeen/weather-app.git\](https://github.com/yahyamobeen/weather-app.git)  
cd weather-app

### **2\. Set Up Virtual Environment (Optional but Recommended)**

\# Windows  
python \-m venv .venv  
.venv\\Scripts\\activate

\# Mac/Linux  
python3 \-m venv .venv  
source .venv/bin/activate

### **3\. Install Dependencies**

pip install \-r requirements.txt

### **4\. Configure Environment Variables**

Create a .env file in the root directory and add your WeatherAPI key:

Weather\_API\_KEY=your\_api\_key\_here

*(You can get a free API key from [weatherapi.com](https://www.weatherapi.com/))*

### **5\. Run the Server**

uvicorn main\_weather:app \--reload

## **📖 Usage**

### **Using the Interface**

1. Open your browser and go to http://127.0.0.1:8000/static/.  
2. Enter a city name (e.g., "London" or "Lahore") in the input box.  
3. Click **"Get Weather"** to see the current temperature.

### **API Documentation (Swagger UI)**

FastAPI automatically generates interactive API documentation.

* Go to http://127.0.0.1:8000/docs to test the endpoints directly.

**Example Endpoint:** POST /weather/

**Request Body:**

{  
  "city": "London"  
}

**Response:**

{  
  "city": "London",  
  "temperature": 15.0  
}

## **🤝 Contributing**

Contributions are welcome\! Feel free to fork the repository and submit a pull request.

1. Fork the Project  
2. Create your Feature Branch (git checkout \-b feature/AmazingFeature)  
3. Commit your Changes (git commit \-m 'Add some AmazingFeature')  
4. Push to the Branch (git push origin feature/AmazingFeature)  
5. Open a Pull Request

## **📜 License**

This project is open-source and available for educational purposes.