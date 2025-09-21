# Titanic Survival Prediction - MLOps Pipeline

## Quick Start

### Option A: Manual Pipeline
```bash
# 1. Setup Environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# 2. Run Data Pipeline
python code/datasets/data_preprocessing.py
python code/models/train_model.py

# 3. Deploy Application
cd code/deployment
docker-compose up -d
```

### Option B: Automated Airflow Pipeline

#### Prerequisites
- Docker and Docker Compose installed
- Ports 8080, 8000, 8501 available

#### Step-by-Step Setup
```bash
# 1. Navigate to Airflow directory
cd services/airflow

# 2. Build custom Airflow image (3-5 minutes)
docker-compose build

# 3. Start PostgreSQL
docker-compose up postgres -d
# Wait 10-15 seconds

# 4. Initialize Airflow database
docker-compose run --rm airflow-webserver airflow db init

# 5. Create admin user
docker-compose run --rm airflow-webserver airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin

# 6. Start all Airflow services
docker-compose up -d

# 7. Check status
docker-compose ps
```

## Access Points

**Manual Setup:**
- Web App: http://localhost:8501
- API: http://localhost:8000

**Airflow Setup:**
- Airflow UI: http://localhost:8080 (admin/admin)
- Automated Apps: http://localhost:8000 & http://localhost:8501 (after pipeline runs)

## Automated MLOps Pipeline

The Airflow pipeline (`titanic_mlops_pipeline`) runs every 5 minutes and includes:

1. **Data Engineering**: Processes raw Titanic data
2. **Model Engineering**: Trains RandomForest model (~83% accuracy) 
3. **Deployment**: Automatically deploys API and Web app

### Monitoring
- View pipeline status in Airflow UI
- Check logs: `docker-compose logs airflow-scheduler -f`
- Manual trigger available in Airflow UI

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
