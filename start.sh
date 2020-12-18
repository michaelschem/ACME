python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations api
python manage.py migrate
python manage.py createsuperuser --email admin@schempc.com --username admin
python manage.py loaddata api/fixtures/api.yaml
sh test.sh
python manage.py runserver &
open http://127.0.0.1:8000/