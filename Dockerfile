FROM python:3

EXPOSE 5000

WORKDIR /var/www/

COPY . /var/www/flask-template

RUN pip install --upgrade pip
RUN pip install -r flask-template/requirements.txt
RUN pip install gunicorn
RUN ls

CMD gunicorn -b 0.0.0.0:5000 'flask-template.api.main:create_app()'
