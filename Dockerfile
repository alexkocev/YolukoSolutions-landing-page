FROM python:3.11.4-slim

# Install necessary build tools and libcairo2
RUN apt-get update && \
    apt-get install -y gcc python3-dev libcairo2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the requirements.txt first
COPY requirements.txt .

# Upgrade pip and install the required packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0", "--server.port", "8088"]