set -o errexit
REQUIREMENTS_FILE="./env/requirements.txt"

# Installer les dépendances à partir de requirements.txt
pip install -r "$REQUIREMENTS_FILE"

python manage.py collectstatic --no-input
python manage.py migrate
