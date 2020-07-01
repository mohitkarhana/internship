# internship
sudo apt-get install virtualenv
virtual env -p python3 env
source env/bin/activate
pip install django
pip install requirements.txt
make your database name as internship by using postgresl and configure it
python manage.py makemigrations
python manage.py migrate
