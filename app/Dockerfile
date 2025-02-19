# basic image
FROM python:3.9-slim

# Arbeitsverzeichnis
WORKDIR /app

# Abhängigkeiten
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app-code
COPY app.py .

# port freigeben
EXPOSE 5000

# start app
CMD ["python", "app.py"]