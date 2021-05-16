.PHONY: build
build:
	docker build -t jordanbertasso/linux-challenges-test .

.PHONY: run
run:
	docker run --rm -it -v $(pwd):/host jordanbertasso/linux-challenges-test 

.PHONY: all
all:
	$(MAKE) build && $(MAKE) run