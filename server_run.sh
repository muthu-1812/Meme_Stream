cd ${usr}-me_buildout_xmeme

# sorr  had to add this here as some req where not being installed
pip install -r requirements.txt 




python3 manage.py flush

rm db.sqlite3  

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py collectstatic

echo "Starting server"

python3 manage.py runserver 0.0.0.0:8081

echo "server started"
