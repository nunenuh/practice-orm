.PHONY: rundb restartdb stopdb

rundb:
	docker-compose up -d

restartdb:
	docker-compose restart

stopdb:
	docker-compose down