# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-alpine3.14
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

COPY ./app /app

COPY requirements/base.txt requirements.txt

EXPOSE 8000

RUN pip install -r requirements.txt

# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]