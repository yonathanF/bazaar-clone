chmod 777 -R /app 
pip install -r /app/models/requirements.txt 
python /app/models/manage.py migrate 
cd models 
python /app/models/manage.py flush --noinput 
python /app/models/manage.py loaddata /app/models/fixtures/db.json 
mod_wsgi-express start-server --working-directory /app/models --reload-on-changes /app/models/models/wsgi.py
