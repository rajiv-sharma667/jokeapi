# Joke API Project

## Description
This project is a Django application that fetches jokes from the JokeAPI, processes the data, and stores it in a SQLite database. The application provides an API endpoint to trigger the fetching and storing of jokes.

## Steps Performed

### Step 1: Set Up Project Directory
- Created a new directory for the project:
  mkdir joke_api_project
  cd joke_api_project

### Step 2: Create a Virtual Environment and activated it
- python -m venv venv

### Step 3: Install Required Packages
- Django
- djangorestframework
- requests

### Step 4: Create a Django Project and Django App
- django-admin startproject joke_api
- cd joke_api
- python manage.py startapp jokes

### Step 5: Update setting
- In installed_apps

### Step 6: Create the Joke Model
- Created and applied migrations to set up the database

### Step 7: Create API view and written logic in view.py and serializer.py

### Step 8: Configure URLs
- Added the URL for the API view in jokes/urls.py
- Included the jokes app URLs in the main project urls.py

### Step 9: Run the Server and test the API
- http://127.0.0.1:8000/jokes/fetch-jokes/