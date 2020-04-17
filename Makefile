up:
	docker-compose -f docker-compose.yml up --build

down:
	docker-compose -f docker-compose.yml down

test:
	docker-compose -f docker-compose.yml build
	docker-compose -f docker-compose.yml run --rm app sh entrypoints/test.sh
	docker-compose -f docker-compose.yml down

build:
	docker-compose -f docker-compose.yml build

deploy_heroku:
	docker pull registry.heroku.com/moviewarehouse-app/web:latest
	docker build -t app ./app --cache-from registry.heroku.com/moviewarehouse-app/web:latest
	docker tag app registry.heroku.com/moviewarehouse-app/web:latest
	docker push registry.heroku.com/moviewarehouse-app/web:latest
	heroku container:release -a moviewarehouse-app web
	heroku run python manage.py migrate -a moviewarehouse-app

.PHONY: up down test build deploy_heroku
