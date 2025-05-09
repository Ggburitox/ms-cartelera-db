FROM python:3.10
WORKDIR /app
COPY create_db.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "create_db.py"]
