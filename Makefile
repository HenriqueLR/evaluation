all: test

clean:
	@find . -name "*.pyc" | xargs rm -f

test: clean
	./manage.py test

database:
	./manage.py migrate
	./manage.py syncdb

run: clean
	./manage.py runserver 0.0.0.0:7000
