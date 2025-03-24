build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

migrate:
	docker-compose exec web sh -c "cd /app/APIHub && python manage.py migrate"

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

logs:
	docker-compose logs -f

shell:
	docker-compose exec web sh -c "cd /app/APIHub && python manage.py shell"
