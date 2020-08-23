How to run:
- git clone https://github.com/edurra/gitsinfo.git
- cd gitsinfo/server
- docker build -t gitsinfo .
- docker run --name gitsinfo -p 8000:8000 gitsinfo

Without docker:

- Python >= 3.6 is required
- git clone https://github.com/edurra/gitsinfo.git
- cd gistnifo/server
- pip3 install -r requirements.txt
- export DJANGOKEY=$(openssl rand -base64 20)
- cd gitsinfo
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py runserver

The server will be listening on port 8000

