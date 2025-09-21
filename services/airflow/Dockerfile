FROM apache/airflow:2.7.0

# Switch to root to install system packages
USER root

# Install Docker CLI and requirements
RUN apt-get update && \
    apt-get install -y docker.io curl && \
    rm -rf /var/lib/apt/lists/*

# Add airflow user to docker group
RUN usermod -aG docker airflow

# Switch back to airflow user
USER airflow

# Copy and install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy project requirements
COPY ../../requirements.txt /workspace-requirements.txt
RUN pip install --no-cache-dir -r /workspace-requirements.txt