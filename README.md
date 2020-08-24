# Introduction

# How to run
## Prerequisites

In order to run the server, it is necesary to have [Docker Compose](https://docs.docker.com/compose/) installed.

## In the command line
```
git clone https://github.com/edurra/gitsinfo.git
cd gitsinfo/server
docker-compose up
```
# How to use

The server will have default credentials admin/admin. The admin portal is located at http://SERVER_IP:8000/admin.
Change the admin password and create new users.

Once logged in the application portal (http://SERVER_IP:800), you can scan repositories or see the history of previous scans. You can also configure a periodic scan for the repositories (1 day delay between scans).
