FROM python:3.12-slim
RUN apt-get update && apt-get install -y \
    google-chrome-stable libnss3 libgconf-2-4 xvfb \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt && playwright install chromium
COPY . .
ENV DISPLAY=:99 HEADLESS=true
CMD ["python", "scanner.py", "--tier1", "--json"]
