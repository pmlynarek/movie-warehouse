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

.PHONY: up down test build
