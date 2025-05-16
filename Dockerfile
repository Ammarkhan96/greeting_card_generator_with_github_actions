FROM python:3.9-slim-buster

WORKDIR /app

COPY greeting_generator.py .

CMD ["python", "greeting_generator.py"]