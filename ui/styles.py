"""
Custom CSS styles for Smart Doctor's Assistant
Ultra-modern, responsive, production-ready styling
"""

def get_custom_css():
    return """
    <style>
    /* Import Premium Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    /* ============================================
       GLOBAL RESET & BASE STYLES
    ============================================ */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }
    
    html, body {
        scroll-behavior: smooth;
    }
    
    /* Main container with animated gradient background */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        position: relative;
    }
    
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(100px);
        z-index: 0;
    }
    
    .main > div {
        position: relative;
        z-index: 1;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* ============================================
       TYPOGRAPHY
    ============================================ */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        letter-spacing: -0.02em;
    }
    
    h1 {
        font-size: clamp(2rem, 5vw, 3.5rem);
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        font-weight: 800;
        line-height: 1.2;
    }
    
    /* ============================================
       SIDEBAR - GLASSMORPHISM DESIGN
    ============================================ */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, 
            rgba(102, 126, 234, 0.95) 0%, 
            rgba(118, 75, 162, 0.95) 100%);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    [data-testid="stSidebar"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
        opacity: 0.3;
    }
    
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #ffffff !important;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    [data-testid="stSidebar"] .stButton button {
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: white !important;
        border-radius: 12px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
        font-weight: 500;
        padding: 0.75rem 1rem;
    }
    
    [data-testid="stSidebar"] .stButton button:hover {
        background: rgba(255, 255, 255, 0.25);
        border-color: rgba(255, 255, 255, 0.5);
        transform: translateX(5px) scale(1.02);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
    }
    
    [data-testid="stSidebar"] .stButton button:active {
        transform: translateX(3px) scale(0.98);
    }
    
    /* Sidebar slider styling */
    [data-testid="stSidebar"] .stSlider {
        padding: 1.5rem 0;
    }
    
    /* ============================================
       INPUT ELEMENTS
    ============================================ */
    .stTextArea textarea {
        border: 2px solid transparent;
        border-radius: 16px;
        padding: 1.25rem;
        font-size: 1rem;
        transition: all 0.3s ease;
        background: white;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        line-height: 1.6;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.2),
                    0 0 0 4px rgba(102, 126, 234, 0.1);
        transform: translateY(-2px);
    }
    
    .stTextArea textarea::placeholder {
        color: #94a3b8;
        font-style: italic;
    }
    
    /* ============================================
       BUTTONS - MODERN GRADIENT DESIGN
    ============================================ */
    .stButton button {
        border-radius: 14px;
        font-weight: 600;
        padding: 0.875rem 2rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: none;
        font-size: 1.05rem;
        letter-spacing: 0.01em;
        position: relative;
        overflow: hidden;
    }
    
    .stButton button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s;
    }
    
    .stButton button:hover::before {
        left: 100%;
    }
    
    .stButton button[kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    }
    
    .stButton button[kind="primary"]:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
    }
    
    .stButton button[kind="primary"]:active {
        transform: translateY(-1px) scale(0.98);
    }
    
    .stButton button[kind="secondary"] {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        box-shadow: 0 10px 30px rgba(240, 147, 251, 0.4);
    }
    
    .stButton button[kind="secondary"]:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 15px 40px rgba(240, 147, 251, 0.5);
    }
    
    /* ============================================
       FILE UPLOADER - DRAG & DROP ZONE
    ============================================ */
    [data-testid="stFileUploader"] {
        background: white;
        border: 3px dashed #cbd5e1;
        border-radius: 20px;
        padding: 2rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: #667eea;
        background: linear-gradient(135deg, #f8f9ff 0%, #f0f4ff 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.15);
    }
    
    /* ============================================
       RESULT CARDS - GLASSMORPHISM
    ============================================ */
    .result-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.5);
        margin-bottom: 2rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .result-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    }
    
    .result-card:hover {
        box-shadow: 0 30px 80px rgba(0, 0, 0, 0.15);
        transform: translateY(-5px);
    }
    
    .result-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #e2e8f0;
    }
    
    .result-icon {
        width: 56px;
        height: 56px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
    }
    
    .result-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1e3a5f;
        margin: 0;
    }
    
    .result-section {
        background: linear-gradient(135deg, #f8f9ff 0%, #f0f4ff 100%);
        border-left: 5px solid #667eea;
        padding: 1.75rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 10px rgba(102, 126, 234, 0.08);
    }
    
    .result-section h3 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1.15rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 8px;
        font-weight: 700;
    }
    
    .result-section p {
        color: #475569;
        line-height: 1.7;
        margin: 0;
    }
    
    .badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .badge-knowledge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .badge-symptoms {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(240, 147, 251, 0.3);
    }
    
    .badge-both {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(79, 172, 254, 0.3);
    }
    
    /* Query display */
    .query-display {
        background: linear-gradient(135deg, #f8f9ff 0%, #ede9fe 100%);
        border-left: 5px solid #667eea;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        font-style: italic;
        color: #1e293b;
        font-weight: 500;
        box-shadow: 0 2px 10px rgba(102, 126, 234, 0.1);
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #0066cc !important;
    }
    
    /* Slider styling */
    .stSlider {
        padding: 1rem 0;
    }
    
    /* Success message */
    .stSuccess {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        color: #065f46;
        border-left: 4px solid #10b981;
    }
    
    /* Error message */
    .stError {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        color: #991b1b;
        border-left: 4px solid #ef4444;
    }
    
    /* Info message */
    .stInfo {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        color: #1e40af;
        border-left: 4px solid #3b82f6;
    }
    
    /* Warning message */
    .stWarning {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        color: #92400e;
        border-left: 4px solid #f59e0b;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(241, 245, 249, 0.5);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5568d3 0%, #653a8b 100%);
    }
    
    /* Card container */
    .card-container {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
        margin-bottom: 1.5rem;
    }
    
    /* Feature badge */
    .feature-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 255, 255, 0.9);
        border: 2px solid rgba(102, 126, 234, 0.3);
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 600;
        color: #667eea;
        margin-right: 0.5rem;
        margin-bottom: 0.75rem;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.15);
        transition: all 0.3s ease;
    }
    
    .feature-badge:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.25);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    /* Disclaimer */
    .disclaimer {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 4px solid #f59e0b;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        margin-top: 2rem;
        font-size: 0.875rem;
        color: #92400e;
    }
    
    /* Animation */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .result-card {
        animation: fadeIn 0.4s ease-out;
    }
    
    /* ============================================
       RESPONSIVE DESIGN - MOBILE FIRST
    ============================================ */
    
    /* Tablet and below */
    @media (max-width: 1024px) {
        .main {
            padding: 1rem;
        }
        
        .result-card {
            padding: 2rem;
        }
        
        .stButton button {
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
        }
    }
    
    /* Mobile devices */
    @media (max-width: 768px) {
        h1 {
            font-size: clamp(1.75rem, 8vw, 2.5rem);
            margin-bottom: 1rem;
        }
        
        .result-card {
            padding: 1.5rem;
            border-radius: 20px;
            margin-bottom: 1.5rem;
        }
        
        .result-icon {
            width: 48px;
            height: 48px;
            font-size: 24px;
        }
        
        .result-section {
            padding: 1.25rem;
            border-radius: 10px;
        }
        
        .result-section h3 {
            font-size: 1rem;
        }
        
        .card-container {
            padding: 1.5rem;
            border-radius: 14px;
        }
        
        .stTextArea textarea {
            padding: 1rem;
            font-size: 0.95rem;
        }
        
        .stButton button {
            padding: 0.75rem 1.25rem;
            font-size: 0.95rem;
        }
        
        .feature-badge {
            font-size: 0.8rem;
            padding: 0.5rem 0.9rem;
        }
        
        .query-display {
            padding: 1rem;
            font-size: 0.9rem;
        }
        
        .disclaimer {
            padding: 0.875rem 1.25rem;
            font-size: 0.8rem;
        }
        
        [data-testid="stFileUploader"] {
            padding: 1.5rem;
            border-radius: 16px;
        }
    }
    
    /* Small mobile devices */
    @media (max-width: 480px) {
        h1 {
            font-size: 1.5rem;
        }
        
        .result-card {
            padding: 1.25rem;
            border-radius: 16px;
        }
        
        .result-header {
            flex-direction: column;
            align-items: flex-start;
            gap: 8px;
        }
        
        .result-icon {
            width: 40px;
            height: 40px;
            font-size: 20px;
        }
        
        .result-section {
            padding: 1rem;
        }
        
        .badge {
            font-size: 0.75rem;
            padding: 0.3rem 0.75rem;
        }
        
        .stButton button {
            padding: 0.65rem 1rem;
            font-size: 0.9rem;
        }
    }
    
    /* Touch device improvements */
    @media (hover: none) and (pointer: coarse) {
        .stButton button,
        [data-testid="stSidebar"] .stButton button,
        .feature-badge {
            min-height: 44px;
            min-width: 44px;
        }
        
        .stTextArea textarea {
            font-size: 16px; /* Prevents zoom on iOS */
        }
    }
    
    </style>
    """

def get_icons():
    """Return emoji icons for various elements"""
    return {
        "doctor": "👨‍⚕️",
        "symptoms": "🩺",
        "knowledge": "📚",
        "both": "🔬",
        "analysis": "🔍",
        "report": "📋",
        "upload": "📄",
        "settings": "⚙️",
        "history": "📜",
        "warning": "⚠️",
        "success": "✅",
        "info": "ℹ️",
        "search": "🔎",
    }
