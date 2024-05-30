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





