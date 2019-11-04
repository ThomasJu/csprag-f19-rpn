prereq:
	pipreqs --force .
test:
	python3 -m unittest
coverage_test:
	coverage run -m unittest
	coverage report

.PHONY: test



# Some Resources 
# Readme cheatsheet https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
# travis link for python https://docs.travis-ci.com/user/languages/python/#examples