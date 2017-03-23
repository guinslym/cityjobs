dev:
	pip install -r requirements/development.txt

git_alias:
	#git config --global alias.st status
	@echo "This will change your git alias. it's better for you to run it yourself"
	@echo "git config --global alias.st status"

dumpdata:
	python manage.py dumpdata --indent 4 > fixtures/data.json
	python manage.py dumpdata emplois --indent 4 > fixtures/db.emplois.json
	@echo 'dumping the Database for backup...we never knows '

test:
	@echo 'Runing py.test -v'
	py.test -v

test_debug:
	@echo 'Runing py.test -x --pdb '
	pytest -x --pdb 
