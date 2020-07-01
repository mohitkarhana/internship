# internship
clone this project
open this projects root directory in terminal and run these cmnds
sudo apt-get install virtualenv
virtual env -p python3 env
source env/bin/activate
cd mysite
pip install -r requirements.txt
make your database name as internship by using postgresl and configure it
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
