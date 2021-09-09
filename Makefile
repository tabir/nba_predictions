CURR_DIR = $(shell pwd)
.PHONY: build push run

build:
	docker build -t tabir/nba_predictions:latest .

push:
	docker push nba_predictions:latest

run:
	docker run -it -v $(CURR_DIR)/input:/input -v $(CURR_DIR)/output:/output  --user=$(id -u):$(id -g) tabir/nba_predictions:latest

