#!/bin/bash
# Create a virtual environment
echo "Creating a virtual environment..."
python -m venv env
source venv/bin/activate

echo "Installing the latest version of pip..."
python -m pip install --upgrade pip

# Build the project
echo "Building the project..."
python -m pip install -r requirements.txt


# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear



