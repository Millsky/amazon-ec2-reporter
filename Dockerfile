FROM tiangolo/uwsgi-nginx-flask:flask-index

COPY ./app /app

RUN pip install boto3