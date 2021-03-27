FROM python:latest

WORKDIR /coursera

COPY . .

RUN pip3 install django

CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]

