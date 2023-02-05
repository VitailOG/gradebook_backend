run-dev:
	python manage.py runserver


migrate:
	python manage.py makemigrations
	python manage.py migrate

rm:
	rm -rf .mypy_cache