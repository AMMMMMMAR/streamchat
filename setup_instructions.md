# AI Chatbot with FastAPI, Streamlit & Gemini

A complete AI chatbot application with a FastAPI backend and Streamlit frontend, powered by Google's Gemini API.

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API key (get it from [Google AI Studio](https://makersuite.google.com/app/apikey))

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Gemini API Key

**Option A: Environment Variable (Recommended)**
```bash
export GEMINI_API_KEY="your-gemini-api-key-here"
```

**Option B: Edit main.py**
Replace `"your-api-key-here"` in `main.py` with your actual API key.

### 3. Run the Application

**Terminal 1 - Start FastAPI Backend:**
```bash
python main.py
```
The API will run on `http://localhost:8000`

**Terminal 2 - Start Streamlit Frontend:**
```bash
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
.
├── main.py           # FastAPI backend
├── app.py            # Streamlit frontend
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## 🎯 Features

- **Real-time Chat**: Ask questions and get AI-powered responses
- **Session Management**: Maintains conversation context
- **Clean UI**: Simple and intuitive Streamlit interface
- **RESTful API**: FastAPI backend with automatic documentation
- **Chat History**: Clear and reset conversation anytime

## 📚 API Endpoints

- `GET /` - API welcome message
- `POST /chat` - Send a message and get a response
- `DELETE /chat/{session_id}` - Clear a chat session
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)

## 🔧 Usage

1. Open the Streamlit app in your browser
2. Type your question in the chat input
3. Press Enter to send
4. View the AI response in real-time
5. Use "Clear Chat History" button to start a new conversation

## 🛠️ Troubleshooting

**API Connection Error:**
- Make sure the FastAPI server is running
- Check that it's running on port 8000
- Verify no firewall is blocking localhost connections

**Gemini API Error:**
- Verify your API key is correct
- Check you have API quota remaining
- Ensure you've enabled the Gemini API in Google Cloud Console

## 📝 Notes

- Chat sessions are stored in memory and will be lost when the server restarts
- For production use, consider adding a database for persistent storage
- The default model is `gemini-pro` - you can change this in `main.py`

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📄 License

MIT License - feel free to use this project however you'd like.