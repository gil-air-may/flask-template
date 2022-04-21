FROM python:3

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

COPY . /var/www/flask-template

RUN pip install --upgrade pip
RUN pip install -r flask-template/requirements.txt
RUN pip install gunicorn
RUN ls

EXPOSE 8000

RUN gunicorn 'flask-template.api.main:create_app()'
