# sudo apt update
# sudo apt -y install python3 python3-pip
# pip3 install django
# cd /usr/local/bin/
# sudo ln -s /home/ubuntu/.local/bin/django-admin.py django-admin
# cd 
# set ALLOWED_HOSTS = ['*'] in settings.py

sudo apt-get install python3-venv
python3 -m venv security3
. security3/bin/activate

python -m pip install django
python manage.py migrate
python manage.py createsuperuser --username=wpedrak --email=wpedrak@wpedrak.com