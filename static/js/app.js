const symptomInput = document.getElementById('symptomInput');
const analyzeBtn = document.getElementById('analyzeBtn');
const pdfInput = document.getElementById('pdfInput');
const uploadArea = document.getElementById('uploadArea');
const indexBtn = document.getElementById('indexBtn');
const temperatureSlider = document.getElementById('temperature');
const topKSlider = document.getElementById('topK');
const tempValue = document.getElementById('tempValue');
const topKValue = document.getElementById('topKValue');
const welcomeMessage = document.getElementById('welcomeMessage');
const resultsContainer = document.getElementById('resultsContainer');
const loadingSpinner = document.getElementById('loadingSpinner');
const historySidebar = document.getElementById('historySidebar');
const toggleHistoryBtn = document.getElementById('toggleHistory');
const closeSidebarBtn = document.getElementById('closeSidebar');
const historyList = document.getElementById('historyList');
const clearHistoryBtn = document.getElementById('clearHistory');
const toastContainer = document.getElementById('toastContainer');

let selectedFile = null;

document.addEventListener('DOMContentLoaded', () => {
    setupListeners();
    loadHistory();
});

function setupListeners() {
    analyzeBtn.addEventListener('click', analyzeSymptoms);

    symptomInput.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === 'Enter') {
            analyzeSymptoms();
        }
    });

    uploadArea.addEventListener('click', () => pdfInput.click());
    pdfInput.addEventListener('change', handleFileSelect);
    uploadArea.addEventListener('dragover', handleDragOver);
    uploadArea.addEventListener('dragleave', handleDragLeave);
    uploadArea.addEventListener('drop', handleDrop);
    indexBtn.addEventListener('click', indexPDF);

    temperatureSlider.addEventListener('input', (e) => {
        tempValue.textContent = e.target.value;
    });

    topKSlider.addEventListener('input', (e) => {
        topKValue.textContent = e.target.value;
    });

    toggleHistoryBtn.addEventListener('click', toggleHistory);
    closeSidebarBtn.addEventListener('click', closeHistory);
    clearHistoryBtn.addEventListener('click', clearHistory);
}

async function analyzeSymptoms() {
    const query = symptomInput.value.trim();

    if (!query) {
        showToast('Please enter your symptoms', 'warning');
        return;
    }

    welcomeMessage.style.display = 'none';
    resultsContainer.style.display = 'none';
    loadingSpinner.style.display = 'block';
    analyzeBtn.disabled = true;

    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                query: query,
                temperature: parseFloat(temperatureSlider.value),
                top_k: parseInt(topKSlider.value)
            })
        });

        const data = await response.json();

        if (data.success) {
            displayResults(data.result, data.query);
            loadHistory();
            showToast('Analysis complete', 'success');
        } else {
            throw new Error(data.error || 'Analysis failed');
        }

    } catch (error) {
        console.error('Error:', error);
        showToast(error.message || 'Failed to analyze', 'error');
        welcomeMessage.style.display = 'block';
    } finally {
        loadingSpinner.style.display = 'none';
        analyzeBtn.disabled = false;
    }
}

function displayResults(result, query) {
    const route = result.route || 'N/A';
    const symptomAnalysis = result.symptom_analysis || '';
    const ragSummary = result.rag_summary || '';

    const badgeMap = {
        'knowledge': { class: 'badge-knowledge', icon: '📚', text: 'KNOWLEDGE' },
        'symptoms': { class: 'badge-symptoms', icon: '🩺', text: 'SYMPTOMS' },
        'both': { class: 'badge-both', icon: '🔬', text: 'BOTH' }
    };

    const badge = badgeMap[route] || badgeMap['knowledge'];

    let html = `
        <div class="panel-card result-card">
            <div class="result-header">
                <div class="result-icon-box">📋</div>
                <div>
                    <h2 class="result-title">Analysis Results</h2>
                </div>
            </div>
            
            <div class="query-display">
                <strong>Your Query:</strong>
                ${escapeHtml(query)}
            </div>
            
            <span class="route-badge ${badge.class}">
                ${badge.icon} ${badge.text}
            </span>
    `;

    if (symptomAnalysis) {
        html += `
            <div class="result-section">
                <h3>🩺 Symptom Analysis</h3>
                <p>${escapeHtml(symptomAnalysis)}</p>
            </div>
        `;
    }

    if (ragSummary) {
        html += `
            <div class="result-section">
                <h3>📚 Medical Knowledge Summary</h3>
                <p>${escapeHtml(ragSummary)}</p>
            </div>
        `;
    }

    html += `
            <div class="disclaimer">
                <strong>⚠️ Medical Disclaimer:</strong>
                This analysis is for informational purposes only. Always consult with a qualified healthcare provider for proper diagnosis and treatment.
            </div>
        </div>
    `;

    resultsContainer.innerHTML = html;
    resultsContainer.style.display = 'block';
}

function handleFileSelect(e) {
    const file = e.target.files[0];
    if (file) {
        selectedFile = file;
        updateUploadArea(file.name);
        indexBtn.disabled = false;
    }
}

function handleDragOver(e) {
    e.preventDefault();
    uploadArea.classList.add('dragover');
}

function handleDragLeave(e) {
    e.preventDefault();
    uploadArea.classList.remove('dragover');
}

function handleDrop(e) {
    e.preventDefault();
    uploadArea.classList.remove('dragover');

    const file = e.dataTransfer.files[0];
    if (file && file.type === 'application/pdf') {
        selectedFile = file;
        pdfInput.files = e.dataTransfer.files;
        updateUploadArea(file.name);
        indexBtn.disabled = false;
    } else {
        showToast('Please upload a PDF file', 'warning');
    }
}

function updateUploadArea(filename) {
    uploadArea.querySelector('.upload-text').textContent = filename;
}

async function indexPDF() {
    if (!selectedFile) {
        showToast('Please select a PDF file', 'warning');
        return;
    }

    console.log('Starting PDF upload:', selectedFile.name);

    const formData = new FormData();
    formData.append('file', selectedFile);

    indexBtn.disabled = true;
    indexBtn.textContent = 'Indexing...';

    try {
        console.log('Sending upload request...');
        const response = await fetch('/api/upload', {
            method: 'POST',
            body: formData
        });

        console.log('Response status:', response.status);

        if (!response.ok) {
            const errorText = await response.text();
            console.error('Server error:', errorText);
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        console.log('Response data:', data);

        if (data.success) {
            showToast(data.message, 'success');
            selectedFile = null;
            pdfInput.value = '';
            uploadArea.querySelector('.upload-text').textContent = 'Click or drag PDF';
        } else {
            throw new Error(data.error || 'Failed to index PDF');
        }

    } catch (error) {
        console.error('Upload error:', error);
        showToast(error.message || 'Failed to index PDF', 'error');
    } finally {
        indexBtn.disabled = true;
        indexBtn.textContent = 'Index PDF';
    }
}

function toggleHistory() {
    historySidebar.classList.toggle('active');
}

function closeHistory() {
    historySidebar.classList.remove('active');
}

async function loadHistory() {
    try {
        const response = await fetch('/api/history');
        const data = await response.json();

        if (data.success && data.history.length > 0) {
            displayHistory(data.history);
        } else {
            historyList.innerHTML = '<p class="history-empty">No queries yet</p>';
        }
    } catch (error) {
        console.error('Error loading history:', error);
    }
}

function displayHistory(history) {
    const html = history.reverse().map((item, index) => {
        const route = item.result.route || 'N/A';
        const query = item.query.length > 60 ? item.query.substring(0, 60) + '...' : item.query;

        return `
            <div class="history-item" onclick="loadHistoryItem(${history.length - 1 - index})">
                <div class="history-item-query">${escapeHtml(query)}</div>
                <div class="history-item-route">Route: ${route.toUpperCase()}</div>
            </div>
        `;
    }).join('');

    historyList.innerHTML = html;
}

async function loadHistoryItem(index) {
    try {
        const response = await fetch('/api/history');
        const data = await response.json();

        if (data.success && data.history[index]) {
            const item = data.history[index];
            symptomInput.value = item.query;
            displayResults(item.result, item.query);
            closeHistory();
        }
    } catch (error) {
        console.error('Error loading history item:', error);
    }
}

async function clearHistory() {
    if (!confirm('Are you sure you want to clear all history?')) {
        return;
    }

    try {
        const response = await fetch('/api/clear-history', {
            method: 'POST'
        });

        const data = await response.json();

        if (data.success) {
            historyList.innerHTML = '<p class="history-empty">No queries yet</p>';
            showToast('History cleared', 'success');
        }
    } catch (error) {
        console.error('Error clearing history:', error);
        showToast('Failed to clear history', 'error');
    }
}

function showToast(message, type = 'success') {
    const icons = {
        success: '✅',
        error: '❌',
        warning: '⚠️'
    };

    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `
        <span class="toast-icon">${icons[type]}</span>
        <span class="toast-message">${escapeHtml(message)}</span>
    `;

    toastContainer.appendChild(toast);

    setTimeout(() => {
        toast.style.animation = 'slideIn 0.3s ease-out reverse';
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

window.loadHistoryItem = loadHistoryItem;
