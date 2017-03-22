
git config --global alias.st status
python manage.py dumpdata --indent 4 > data.json
python manage.py dumpdata emplois --indent 4 > db.emplois.json
python manage.py loaddata db_emplois.json
django-admin makemessages --locale=de --extension xhtml
./manage.py dumpdata auth.user --indent 2 --format xml > user.xml
./manage.py dumpdata admin.logentry > logentry.json
Following command will dump only the content in django admin.logentry table
Python path

setup:
	pip install -e .
	pip install -r requirements/dev.txt

setup_ci:
	pip install -e .
	pip install -r requirements/ci.txt

ci: test lint typing
	@echo "CI complete"

lint:
	@echo "Running pylint"
	@pylint python_template tests pylint_custom --msg-template="{path}:{line}:{column} {msg_id}({symbol}) {msg}"

test:
	@echo "Running pytest"
	@py.test tests

typing:
	@echo "Running mypy"
	@mypy python_template pylint_custom tests --ignore-missing-imports