# Gemini Chatbot

A real-time chatbot powered by Google's Gemini API, built with FastAPI and Streamlit.

## Features
- Real-time chat interface
- Session management
- Powered by Google's Gemini AI
- Simple and intuitive UI

## Prerequisites
- Python 3.8+
- Google Gemini API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your Gemini API key:
   ```
   GEMINI_API_KEY=your-api-key-here
   ```

## Running the Application

1. Start the FastAPI backend:
   ```bash
   uvicorn fastapi_backend:app --reload
   ```

2. In a new terminal, start the Streamlit frontend:
   ```bash
   streamlit run streamlit_frontend.py
   ```

3. Open your browser and go to `http://localhost:8501`

## Project Structure
```
.
├── fastapi_backend.py     # FastAPI backend
├── streamlit_frontend.py  # Streamlit frontend
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
└── README.md             # This file
```

## License
MIT
