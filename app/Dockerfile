FROM python:3.11-alpine
WORKDIR /app
ENV FLASK_APP=examapi.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]