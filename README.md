# 👨‍⚕️ Smart Doctor's Assistant

**AI-Powered Medical Analysis with RAG Technology & Web Search**

A professional, production-ready medical assistant application built with **Flask**, **Google Gemini**, **LangChain**, and **ChromaDB**. Features a modern, single-page UI, intelligent symptom analysis, and comprehensive medical knowledge retrieval from both local documents and the web.

---

## ✨ Features

### Core Functionality
- 🩺 **Intelligent Symptom Analysis** - Advanced AI-powered symptom interpretation using Gemini Flash/Pro.
- 📚 **Medical Knowledge Retrieval (RAG)** - Context-aware medical information from indexed documents.
- 🌐 **Google Search Integration** - Real-time web search to supplement local knowledge with the latest medical information.
- 🔬 **Smart Router Chain** - Automatically routes queries to symptoms analyzer, knowledge base, or both.
- 📄 **PDF Document Ingestion** - Upload and index medical reports, research papers, and clinical documents via drag-and-drop.
- 💾 **Vector Database** - Efficient semantic search using ChromaDB embeddings.
- 📜 **Query History** - Track and revisit previous analyses with a collapsible sidebar.

### Modern UI/UX
- 🎨 **Stunning Gradient Design** - Animated gradient background with glassmorphism effects.
- 📱 **Fully Responsive** - Works seamlessly on desktop, tablet, and mobile devices.
- ⚡ **Single Page Application** - No page reloads, smooth transitions, and single-screen layout (no scrollbars).
- 🔍 **Interactive Results** - Beautiful card-based result display with clear visual hierarchy and formatted text.
- 🔔 **Toast Notifications** - Real-time feedback with elegant toast messages.
- ⚙️ **Customizable Settings** - Adjust AI temperature and retrieval parameters (Top-K).

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Smart_Doctors_Assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

4. **Run the application**
   ```bash
   python flask_app.py
   ```

5. **Access the app**
   Open your browser and navigate to `http://localhost:5000`

---

## 📖 Usage Guide

### 1. Analyze Symptoms
- Enter your symptoms or medical questions in the text area.
- Adjust settings (Temperature and Top-K) if needed.
- Click **"🔍 Analyze Symptoms"**.
- View comprehensive results including:
    - **Symptom Analysis**: Possible conditions, severity, actions, warning signs.
    - **Medical Knowledge**: Information from indexed PDFs.
    - **Web Search Results**: Relevant information from Google Search.

### 2. Upload Medical Documents
- Drag and drop a PDF file into the upload area or click to select.
- Click **"Index PDF"** to add it to the knowledge base.
- The system will process and index the document for future queries.

### 3. View History
- Click the floating **"📜"** button in the bottom-right corner.
- Browse your recent queries.
- Click any history item to reload that analysis.
- Clear history with the "Clear History" button.

---

## 🏗️ Project Structure

```
Smart_Doctors_Assistant/
├── flask_app.py              # Flask backend application
├── templates/
│   └── index.html           # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css        # Modern CSS styling
│   └── js/
│       └── app.js           # Frontend JavaScript
├── core/                    # Core functionality
│   ├── config.py           # Configuration settings
│   ├── logger.py           # Logging setup
│   └── vector_db.py        # ChromaDB vector store
├── services/               # Business logic
│   ├── embedder.py         # PDF embedding service
│   ├── final_report.py     # Report generation
│   ├── google_search.py    # Google Search service
│   ├── rag_engine.py       # RAG retrieval engine
│   └── symptom_engine.py   # Symptom analysis engine
├── uploads/                # Uploaded PDF files
├── chroma_db/              # Vector database storage
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🛠️ Recent Improvements

### UI Overhaul
- **Single-Screen Layout**: Eliminated scrollbars on the main body; optimized spacing and layout to fit within the viewport.
- **Clean Code**: Simplified HTML, CSS, and JS for better readability and maintainability.
- **Visual Polish**: Enhanced gradients, shadows, and typography.

### RAG & Analysis Enhancements
- **Detailed Responses**: Improved prompts to generate comprehensive, structured medical responses (bullet points, sections).
- **Google Search**: Integrated Google Search to fetch up-to-date information from the web.
- **Symptom Analysis**: Structured output covering possible conditions, severity, actions, warning signs, and self-care.
- **Top-K**: Increased default retrieval count to 10 for richer context.

### Fixes
- **PDF Upload**: Restored and fixed the PDF upload functionality with better error handling and logging.
- **Dependencies**: Added `googlesearch-python` and `beautifulsoup4`.

---

## ⚠️ Medical Disclaimer

This application is for **informational and educational purposes only** and should not replace professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

---

**Built with ❤️ using Flask, Google Gemini AI, and Modern Web Technologies**