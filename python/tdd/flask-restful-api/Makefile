# Welcome to the make file, the first (and default) task is "make
# all", and it just runs "make dependencies" and "make test"

all: dependencies test

# Runs the unit and functional tests
test: unit functional

# Install dependencies
dependencies:
	pip install -r requirements.txt

# runs unit tests

unit:
	tumbler unit

# runs functional tests

functional:
	tumbler functional

# runs the server, exposing the routes
run:
	tumbler run --host 0.0.0.0 routes.py
