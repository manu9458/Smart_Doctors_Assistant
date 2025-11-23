FROM python:3.11-slim

# 1. Set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stderr (logs appear immediately)
ENV PYTHONUNBUFFERED=1

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies
# build-essential and git are often needed for installing certain python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# 4. Install Python dependencies
COPY requirements.txt .
# We install gunicorn explicitly here since it wasn't in your requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn

# 5. Copy the rest of the application code
COPY . .

# 6. Create necessary directories (e.g., for uploads) to ensure they exist
RUN mkdir -p uploads chroma_db

# 7. Expose the port (Documentary only)
EXPOSE 5000

# 8. Run the application with Gunicorn (Production Server)
# --bind 0.0.0.0:${PORT:-5000}: Listens on the port Render assigns (or 5000 locally)
# --workers 2: Handles multiple concurrent requests
# --timeout 120: Gives the AI longer to process PDF uploads before timing out
CMD gunicorn --bind 0.0.0.0:${PORT:-5000} --workers 2 --timeout 120 flask_app:app