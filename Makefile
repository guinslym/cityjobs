dev:
	pip install -r requirements/development.txt

git_alias:
	git config --global alias.st status

dumpdata:
	python manage.py dumpdata --indent 4 > fixtures/data.json
	python manage.py dumpdata emplois --indent 4 > fixtures/db.emplois.json
	@echo 'dumping the Database for backup...we never knows '
