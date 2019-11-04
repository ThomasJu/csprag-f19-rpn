prereq:
	pipreqs --force .
test:
	python3 -m unittest
coverage_test:
	coverage run -m unittest
	coverage report

.PHONY: test