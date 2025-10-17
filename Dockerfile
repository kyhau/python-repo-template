FROM python:3.13-slim
LABEL maintainer="virtualda@gmail.com"

WORKDIR /opt/apps/app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy dependency files first for better layer caching
COPY pyproject.toml poetry.lock ./

# Install dependencies only (without the package)
RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-root && \
    rm -rf /root/.cache/pip

# Copy application code
COPY app/ ./app/

# Install the package itself
RUN poetry install --only-root

# Call app's main entry point defined in pyproject.toml
# CMD ["app-cli"]
