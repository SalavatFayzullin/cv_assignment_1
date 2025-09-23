FROM python:3.11-slim

WORKDIR /app

COPY code/deployment/api/requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p /app/models
COPY models/titanic_model.pkl /app/models/titanic_model.pkl

COPY code/deployment/api/main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]