set -o errexit
REQUIREMENTS_FILE="./env/requirements.txt"
MANAGE_FILE="Projet_2CS/NewEsi/manage.py"
# Installer les dépendances à partir de requirements.txt
pip install -r "$REQUIREMENTS_FILE"

# Collect static files
python "$MANAGE_FILE" collectstatic --no-input

# Apply database migrations
python "$MANAGE_FILE" migrate