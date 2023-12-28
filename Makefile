up:
	docker-compose up -d

down:
	docker-compose down

install-generator-requirements:
	cd Generator && virtualenv venv && source venv/bin/activate && pip3 install -r requirements.txt

install-main-requirements:
	virtualenv venv && source venv/bin/activate && pip3 install -r requirements.txt

run-generator:
	cd Generator && source venv/bin/activate && python3 main.py

run-main:
	source venv/bin/activate && python3 main.py