from flask import Flask, render_template, request, jsonify
import os
from core.config import Settings
from core.logger import get_logger
from core.vector_db import load_vector_db
from services.embedder import embed_pdf
from services.final_report import generate_report

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

settings = Settings()
logger = get_logger()
vector_db = load_vector_db(settings)

chat_history = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        temperature = float(data.get('temperature', settings.DEFAULT_TEMP))
        top_k = int(data.get('top_k', settings.DEFAULT_TOP_K))
        
        if not query:
            return jsonify({'error': 'Please enter your symptoms'}), 400
        
        output = generate_report(
            query=query,
            vector_store=vector_db,
            settings=settings,
            temperature=temperature,
            top_k=top_k,
        )
        
        if not output or (not output.get("rag_summary") and not output.get("symptom_analysis")):
            output = {
                "route": "knowledge",
                "rag_summary": "Unable to generate a response. Please try rephrasing your question.",
            }
        
        entry = {
            "query": query,
            "result": output,
        }
        chat_history.append(entry)
        
        return jsonify({
            'success': True,
            'result': output,
            'query': query
        })
        
    except Exception as e:
        logger.error(f"Error in analyze: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/upload', methods=['POST'])
def upload_pdf():
    try:
        logger.info("Upload request received")
        
        if 'file' not in request.files:
            logger.error("No file in request")
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        logger.info(f"File received: {file.filename}")
        
        if file.filename == '':
            logger.error("Empty filename")
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith('.pdf'):
            logger.error(f"Invalid file type: {file.filename}")
            return jsonify({'error': 'Only PDF files allowed'}), 400
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded.pdf')
        logger.info(f"Saving file to: {filepath}")
        file.save(filepath)
        
        logger.info("Starting PDF embedding")
        count = embed_pdf(filepath, vector_db, settings)
        logger.info(f"Embedded {count} chunks")
        
        if count > 0:
            return jsonify({
                'success': True,
                'message': f'Successfully indexed {count} chunks!'
            })
        else:
            logger.error("No chunks embedded")
            return jsonify({'error': 'Failed to index PDF'}), 500
            
    except Exception as e:
        logger.error(f"Error in upload: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500


@app.route('/api/history', methods=['GET'])
def get_history():
    return jsonify({
        'success': True,
        'history': chat_history[-10:]
    })


@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    global chat_history
    chat_history = []
    return jsonify({'success': True, 'message': 'History cleared'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
