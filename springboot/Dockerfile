FROM openjdk:8-jdk-alpine
LABEL maintainer chegejohn159@gmail.com
COPY target/docker-web-server-1.0.0.jar web-server-1.0.0.jar
ENTRYPOINT ["java","-jar","/web-server-1.0.0.jar"]