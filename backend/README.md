## Workflow

This product is built using the following widely used technologies:

- Flask framework
- Flask-RESTFul

## Quick start
### Using Docker
1. Make sure you have installed [Docker](https://docs.docker.com/get-docker/) installed.
2. After successful installation run the following commands to build the image and run them from the base directory:
  ```
  sudo docker build -t <sudoimage-name of choice> .
  ```
  ```
  sudo docker run <sudoimage-name>
  ```
  3. On successful running,copy the link generated and paste it on your browser to view the app status and test it.
  4. Alternatively, and even better, use `postman` or any other application of your choice to test the APIs.
  5. Note: the APIs rely on the DB to post and fetch data, since the db runs separately as a service, you have to ensure its up and running and linked to the backend via Dockerfile.
  Otherwise you bound to get server error due to timeout as a result of delayed connection.

### Using Flask run
1. Ensure you have all the dependencies in requirements.txt installed using pip
2. Run the application:
  ```
  python3 <base app file(e.g app.py)>
  ```
  - Alternatively:
  Set up the environment
  ```
  export FLASK_APP=<base app file(e.g app.py)>
  ```
  Then:
  ```
  flask run
  ```
