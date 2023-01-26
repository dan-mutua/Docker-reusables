## Dockerize vue and django api

This folder consists of the dockerization files:
+ backend/Dockerfile
+ frontend/Dockerfile
+ frontend/nginx.conf
+ vue-django/docker-compose.yml

Which are required files to dockerize avue based application with a django backend.
It also includes the configuration file for nginx which is the considered reverse proxy server for this
application.

The files can be editted to fit any vuejs project, by replacing values like server name with the correct values
