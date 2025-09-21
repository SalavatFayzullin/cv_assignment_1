# Titanic Survival Prediction - MLOps Pipeline

## Quick Start

### 1. Setup Environment
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Data Pipeline
```bash
python code/datasets/data_preprocessing.py
python code/models/train_model.py
```

### 3. Deploy Application
```bash
cd code/deployment
docker-compose up -d
```

**Access:**
- Web App: http://localhost:8501
- API: http://localhost:8000

### 4. Test Pipeline
```bash
cd services/airflow
python test_pipeline.py
```

## Components

**Main Task:**
- FastAPI model serving
- Streamlit web interface
- Docker containerization

**Extra Task:**
- Automated Airflow pipeline (5-min schedule)
- Data engineering stage
- Model engineering stage  
- Deployment stage
