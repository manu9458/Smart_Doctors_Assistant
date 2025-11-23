# 🩺 Smart Doctor's Assistant

> **Your AI-Powered Medical Companion with Voice Interaction & Document Analysis**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Gemini AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![RAG](https://img.shields.io/badge/Tech-RAG-purple)

**Smart Doctor's Assistant** is a cutting-edge medical analysis tool designed to provide instant, AI-driven insights into symptoms and medical documents. Built with a focus on accessibility and ease of use, it features a **hands-free voice interface**, a modern single-page design, and powerful RAG (Retrieval-Augmented Generation) technology to analyze your personal medical reports.

---

## 🌟 Key Features

### 🗣️ Voice-First Experience
- **Voice Input**: Speak your symptoms naturally using the integrated microphone. No typing required!
- **Voice Assistant**: The AI reads out the analysis to you, acting like a real medical assistant.
- **Hands-Free Control**: Perfect for quick consultations or accessibility needs.

### 🧠 Intelligent Analysis
- **Symptom Checker**: Advanced AI analysis of your symptoms to suggest possible conditions, severity, and home care tips.
- **RAG Technology**: Upload your own medical PDFs (lab reports, prescriptions) to get personalized answers based on *your* data.
- **Smart Context**: Combines general medical knowledge with specific details from your uploaded documents.

### 🎨 Modern & Responsive UI
- **Single-Page Application**: A seamless, scroll-free experience that fits perfectly on any screen.
- **Glassmorphism Design**: Beautiful, modern aesthetics with animated gradients and translucent cards.
- **Real-Time Feedback**: Instant toast notifications and loading states keep you informed.

---

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **AI Model**: Google Gemini Pro (via LangChain)
- **Vector Database**: ChromaDB (for document indexing)
- **Frontend**: HTML5, CSS3 (Glassmorphism), Vanilla JavaScript
- **Speech Services**: Web Speech API (Native Browser Support)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- A Google Cloud API Key (for Gemini)

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/smart-doctors-assistant.git
    cd Smart_Doctors_Assistant
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**
    Create a `.env` file in the root directory and add your API key:
    ```env
    GOOGLE_API_KEY=your_actual_api_key_here
    ```

4.  **Run the Application**
    ```bash
    python flask_app.py
    ```

5.  **Launch**
    Open your browser and visit: `http://localhost:5000`

---

## 📖 How to Use

1.  **Speak or Type**: Click the **"🎤 Voice Input"** button and describe your symptoms, or type them in the box.
2.  **Upload Documents (Optional)**: Drag & drop a medical PDF (e.g., a blood test report) into the upload area and click **"Index PDF"**.
3.  **Analyze**: Click **"🔍 Analyze Symptoms"**.
4.  **Listen & Read**: The AI will generate a detailed report and **read it aloud** to you. You can stop the audio at any time with the "🔇 Stop Voice" button.

---

## 📂 Project Structure

```
Smart_Doctors_Assistant/
├── flask_app.py            # Main Application Entry Point
├── core/                   # Configuration & Database Logic
│   ├── config.py
│   └── vector_db.py
├── services/               # AI & Business Logic
│   ├── rag_engine.py       # RAG Retrieval System
│   ├── symptom_engine.py   # Symptom Analysis Logic
│   ├── embedder.py         # PDF Processing
│   └── final_report.py     # Response Generation
├── static/                 # Frontend Assets
│   ├── css/style.css       # Styling & Animations
│   └── js/app.js           # Voice & UI Logic
├── templates/
│   └── index.html          # Main User Interface
└── uploads/                # Temp storage for PDFs
```

---

## ⚠️ Disclaimer

**This tool is for informational purposes only.**
It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

---

**Created with ❤️ by Manu**