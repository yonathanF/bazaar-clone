chmod 777 -R /app 
pip install django-cors-headers
python /app/bazaar/manage.py migrate 
cd bazaar 
python /app/bazaar/manage.py flush --noinput 
python /app/bazaar/manage.py loaddata /app/bazaar/fixtures/db.json 
mod_wsgi-express start-server --working-directory /app/bazaar --reload-on-changes /app/bazaar/bazaar/wsgi.py
