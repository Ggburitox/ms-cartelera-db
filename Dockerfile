FROM python:3.10

WORKDIR /app
COPY init_db/ ./init_db
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "init_db/create_db.py"]
