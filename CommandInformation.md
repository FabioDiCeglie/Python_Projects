# Conda

conda activate (virtual env)

# Create the Django project

django-admin startproject django_blog .

# Creating an app

django-admin startapp blog

# Running the server

python3 manage.py runserver 8080

# MakeMigrations model

python3 manage.py makemigrations

# Migrate model

python3 manage.py migrate

# Create user

python3 manage.py createsuperuser

# Run Test

python3 manage.py test

# Install packages

pip install -r requirements.txt

# Pre commit install

pre-commit install

# Load data in django project ex:

python manage.py loaddata users.json

# Build Docker Image

docker build -t local/graphql_api:beta .

# Check Docker Image

docker image ls

# Run Docker Image

docker run -p 8000:8000 local/graphql_api:beta

# Stop Dock container

docker container stop (id container)

# List Dock container running

docker container ls

# Docker compose

docker-compose up
