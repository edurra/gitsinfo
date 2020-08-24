FROM python:3.6
ENV DJANGOKEY $(openssl rand -base64 20)
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY ./gitsinfo ./gitsinfo
EXPOSE 8000
WORKDIR gitsinfo
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@gitsinfo.gitsinfo', 'admin')" | python3 manage.py shell
