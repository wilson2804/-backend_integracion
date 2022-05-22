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

EXPOSE 3370
CMD ["python", "manage.py", "runserver", "0.0.0.0:3370"]
