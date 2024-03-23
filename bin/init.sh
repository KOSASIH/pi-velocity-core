#!/bin/bash

# Set the working directory
cd /path/to/project/directory

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
source venv/bin/activate

# Install the project dependencies
pip install -r requirements.txt

# Run the database migrations (if applicable)
python manage.py migrate

# Start the application
python manage.py runserver
