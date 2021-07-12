# PMS-MVP
A simple Parcel Management System MVP

## Workflow

This product is built using the following widely used technologies:

- React.js front-end library
- Flask python backend framework
- MongoDb for database service
- Docker to container service
- Git for versioning

## Quick start Guide
1. Assuming you have got, clone the project into your machine.
2. Find a quick start guide for the respective service in the base directory.
However to run all microservices at once, we use `$ docker-compose.yml file`,
which provides a bus connection to the services.
3. However you can run each service normally in isolation. The documemtation on how to is well documented in each of the respective base repositories. Feel free to explore!

### To Run docker-compose:
Ensure Docker is installed and runs accordingly,
- With Dockerfile for each service well configured run the following commands:
  ```
  $docker-compose build
  ```
- Followed by(Assuming no errors bumped into you!):
  ```
  $docker-compose up
  ```
FYI: The above commands will do you justice by building the images and eventually running the images as per your configuration.
