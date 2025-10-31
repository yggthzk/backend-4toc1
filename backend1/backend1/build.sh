
#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

#'backend1' para ejecutar manage.pyy
python backend1/manage.py collectstatic --no-input
python backend1/manage.py migrate