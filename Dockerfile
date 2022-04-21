FROM python:3

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

ADD . /var/www/flask-template

RUN pip install --upgrade pip
RUN pip install -r flask-template/requirements.txt
RUN pip install gunicorn
RUN pip

EXPOSE 5000

CMD [ "gunicorn", "flask-template.api.main:create"]
