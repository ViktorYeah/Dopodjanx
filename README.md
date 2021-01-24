# Dopodjanx

Dopodjanx is how I call the stack of technologies :

- **Do**cker + **Po**stgreSQL + **Dj**ango + **An**gular + Ngin**x**

### Info
This is a simple web app that shows a list of Famous Companies that went Bankrupt at a certain point in time,
with a useful links to get additional info about them (Checkout Enron documentary).

But the purpouse of this app is actually to show how the forementioned stack of technologies can be organized :)

I also plan to make a video tutorial for this app.

![N|Solid](https://github.com/ViktorYeah/Dopodjanx/blob/master/screenshot.png)

### Installation
The following command should install and run all the services 
```sh
$ sudo docker-compose up
```

### Almost There
Currently the 4 additional steps are required for the app to function properly
In the nearest future I plan to automate these steps with the docker compose, so that no additional tinkering should be required :) 

Create super user 'admin' for the 'dopodjanx' database
```sh
$ sudo docker exec -it <postgres container id> sh
$ su - postgres
$ psql
$ CREATE USER admin WITH PASSWORD 'admin';
$ ALTER USER admin WITH SUPERUSER;
$ GRANT ALL PRIVILEGES ON DATABASE dopodjanx TO admin;
```

Migrate database
```sh
$ sudo docker exec -it <djangoapp container id> sh
$ python3 manage.py migrate
```
Create superuser for Django Admin with the following credentials:
login: **admin**
email: **admin@admin.com**
password: **admin**
```sh
$ python3 manage.py createsuperuser
```
Add data entries to database from **db_data.txt** using Django Admin
```sh
http://127.0.0.1:8105/admin
```
### Links

| Link | Description |
| ------ | ------ |
| http://127.0.0.1:8103 | PG Admin web Interface |
| http://127.0.0.1:8105/admin | Django Admin |
| http://127.0.0.1:8105/companies | API returns information about companies in JSON format |
| http://127.0.0.1:8106 | Main Webapp User Interface |
