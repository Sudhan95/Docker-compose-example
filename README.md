**Set up a multi-container Docker application with Flask as the web service and MySQL as the database service**

Create the following directory structure:

docker_compose_ex/
   - app/
      - Dockerfile
      - app.py
      - requirements.txt
   - docker-compose.yml
  
Setup:
1. install Docker
2. install Docker Compose:
    Copy the appropriate docker-compose binary from GitHub:

      sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

   NOTE: to get the latest version (thanks @spodnet): sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

   Fix permissions after download:

      sudo chmod +x /usr/local/bin/docker-compose

   Verify success:

      docker-compose version
   
**Explaination**

Dockerfile:

. Uses the official Python image.
. Sets the working directory to /app.
. Copies the application files into the container.
. Installs the required Python packages.
. Exposes port 5000.
. Specifies the command to run the Flask application.

docker-compose.yml:
   web service:
   . Builds the Flask application from the app directory.
   . Sets the environment variables for the database connection.
   . Depends on the mysql service to ensure the database starts first.
   mysql service:
   . Uses the official MySQL image.
   . Sets the root password and database name.
   . Maps a volume to persist database data.
   . This setup provides a fully containerized Flask application with a MySQL database, making it easy to manage and deploy.



