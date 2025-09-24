# 1.1 Venv
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# 1.2 Run Data Pipeline
python code/datasets/data_preprocessing.py
python code/models/train_model.py

# 1.3 Deploy Application
cd code/deployment
docker-compose up -d

# 2.1
cd services/airflow
docker-compose up -d --build

# 2.2 Check status
docker-compose ps
