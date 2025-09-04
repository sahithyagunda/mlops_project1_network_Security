FROM python:3.10-slim-bookworm

WORKDIR /app
COPY . /app

# Install required system packages
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install AWS CLI using pip (safer for Python containers)
RUN pip install --no-cache-dir awscli

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
