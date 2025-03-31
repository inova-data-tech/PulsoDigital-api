FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8089"]
