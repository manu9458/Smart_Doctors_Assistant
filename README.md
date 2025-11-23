# 🩺 Smart Doctor's Assistant

> **Your AI-Powered Medical Companion with Document Analysis**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Gemini AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![RAG](https://img.shields.io/badge/Tech-RAG-purple)

**Smart Doctor's Assistant** is a cutting-edge medical analysis tool designed to provide instant, AI-driven insights into symptoms and medical documents. It features a modern single-page design and powerful RAG (Retrieval-Augmented Generation) technology to analyze your personal medical reports.

---

## 🌟 Key Features

### 🧠 Intelligent Analysis
- **Symptom Checker**: Advanced AI analysis of your symptoms to suggest possible conditions, severity, and home care tips.
- **RAG Technology**: Upload your own medical PDFs (lab reports, prescriptions) to get personalized answers based on *your* data.
- **Smart Context**: Combines general medical knowledge with specific details from your uploaded documents.

### 🎨 Modern & Responsive UI
- **Single-Page Application**: A seamless, scroll-free experience that fits perfectly on any screen.
- **Glassmorphism Design**: Beautiful, modern aesthetics with animated gradients and translucent cards.
- **Real-Time Feedback**: Instant toast notifications and loading states keep you informed.
- **Customizable Settings**: Fine-tune the AI's creativity (Temperature) and retrieval depth (Top-K) directly from the UI.

---

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **AI Model**: Google Gemini Pro (via LangChain)
- **Vector Database**: ChromaDB (for document indexing)
- **Frontend**: HTML5, CSS3 (Glassmorphism), Vanilla JavaScript

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

1.  **Enter Symptoms**: Type your symptoms or medical questions in the text box.
2.  **Adjust Settings (Optional)**: Use the sliders to control:
    *   **Temperature**: Higher values for more creative/varied answers, lower for more focused ones.
    *   **Top-K**: How many document chunks to retrieve for analysis.
3.  **Upload Documents (Optional)**: Drag & drop a medical PDF (e.g., a blood test report) into the upload area and click **"Index PDF"**.
4.  **Analyze**: Click **"🔍 Analyze Symptoms"**.
5.  **Read Results**: The AI will generate a detailed report, separating symptom analysis from document-based insights.

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
│   └── js/app.js           # UI Logic
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