
set -o errexit

pip install -r requirements.txt

python backend1/manage.py collectstatic --no-input
python backend1/manage.py migrate