chmod 777 -R /app 
pip install -r /app/experience/requirements.txt 
pip install elasticsearch -U
pip install kafka-python -U
pip install redis
cd experience
python /app/experience/manage.py flush --noinput
mod_wsgi-express start-server --working-directory /app/experience --reload-on-changes /app/experience/experience/wsgi.py
