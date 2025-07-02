# Using lightweight python

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# Install packages
# Update pip and install requirements
# --no-cache-dir to avoid caching and saving space

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

