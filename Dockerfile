FROM python:3.7-slim-buster

WORKDIR /app

COPY . /app

EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
# CMD ["uwsgi", "--ini", "app.ini"]
