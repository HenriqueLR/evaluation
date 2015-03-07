clean:
	@find . -name "*.pyc" | xargs rm -f

database:
	./manage.py migrate
	./manage.py syncdb

run: clean
	./manage.py runserver 0.0.0.0:7000
