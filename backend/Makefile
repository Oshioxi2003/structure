# Makefile for Django project

.PHONY: help run migrate migrations test shell superuser install clean

help:
	@echo "Available commands:"
	@echo "  make run          - Run development server"
	@echo "  make migrate      - Run database migrations"
	@echo "  make migrations   - Create new migrations"
	@echo "  make test         - Run tests"
	@echo "  make shell        - Open Django shell"
	@echo "  make superuser    - Create superuser"
	@echo "  make install      - Install dependencies"
	@echo "  make clean        - Clean pyc files"

run:
	python manage.py runserver

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

test:
	pytest

shell:
	python manage.py shell

superuser:
	python manage.py createsuperuser

install:
	pip install -r requirements/dev.txt

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
