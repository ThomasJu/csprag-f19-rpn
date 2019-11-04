prereq:
	pipreqs --force .
test:
	python3 -m unittest

.PHONY: test