FROM python:3.6
ENV DJANGOKEY $(openssl rand -base64 20)
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY ./gitsinfo ./gitsinfo
EXPOSE 8000
WORKDIR gitsinfo
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000
