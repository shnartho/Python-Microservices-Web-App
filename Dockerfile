FROM python:3.10.0-alpine3.15
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
EXPOSE 5001
HEALTHCHECK --interval=30s --timeout= --start-period= --retries=5 \
            CMD curl -f http://localhost:5001/health || exit 1
ENTRYPOINT ["python", "./src/app.py"]