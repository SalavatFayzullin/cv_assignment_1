FROM apache/airflow:2.7.0

# Switch to root to install system packages
USER root

# Install Docker CLI and docker-compose
RUN apt-get update && \
    apt-get install -y docker.io curl netcat-openbsd && \
    curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
    rm -rf /var/lib/apt/lists/*

# Add airflow user to docker group
RUN usermod -aG docker airflow

# Copy custom entrypoint
COPY entrypoint.sh /entrypoint
RUN chmod +x /entrypoint

# Switch back to airflow user
USER airflow

# Copy and install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Copy project requirements
COPY ../../requirements.txt /workspace-requirements.txt
RUN pip install --no-cache-dir -r /workspace-requirements.txt

ENTRYPOINT ["/entrypoint"]