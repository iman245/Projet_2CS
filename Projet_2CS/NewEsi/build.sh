set -o errexit
REQUIREMENTS_FILE="./env/requirements.txt"

# Install dependencies from requirements.txt
pip install -r "$REQUIREMENTS_FILE"

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Start the application
gunicorn Projet_2CS.NewEsi.NewEsi.wsgi:application

