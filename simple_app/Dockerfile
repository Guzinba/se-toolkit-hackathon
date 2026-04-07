FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir fastapi==0.109.0 uvicorn==0.27.0 sqlmodel==0.0.14 httpx==0.26.0 psycopg2-binary==2.9.9 pydantic==2.5.3 sqlalchemy==2.0.25
COPY main.py .
EXPOSE 9999
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:9999/health')" || exit 1
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9999"]
