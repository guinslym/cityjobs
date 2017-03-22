
git config --global alias.st status
python manage.py dumpdata --indent 4 > data.json
python manage.py dumpdata emplois --indent 4 > db.emplois.json
python manage.py loaddata db_emplois.json
clear