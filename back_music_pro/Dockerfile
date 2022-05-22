FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install psycopg2-binary

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
