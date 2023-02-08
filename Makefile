IMAGENAME=my-image

.PHONY: build all


.DEFAULT_GOAL := all

build:
        @docker build -t ${IMAGENAME} .

all: build




#Source: https://stackoverflow.com/questions/72018386


