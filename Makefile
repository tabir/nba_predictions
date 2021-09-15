CURR_DIR = $(shell pwd)
.PHONY: build push run push_docker push_git

build:
	docker build -t tabir/nba_predictions:latest .

push_docker:
	docker push nba_predictions:latest

push_git:
	git push origin_e

run:
	docker run -it -v $(CURR_DIR)/input:/input -v $(CURR_DIR)/output:/output  --user=$(id -u):$(id -g) tabir/nba_predictions:latest

print-%: ; @echo $*=$($*)
