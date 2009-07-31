commit: update
	svn commit

update:
	svn update

diff:
	svn diff

status:
	svn status

test: 
	rm -rf build
	py.test

clean:
	rm -f core
	find . -name "*.pyc" -print0 | xargs -0 rm -f
	find . -name "svn-commit.*" -print0 | xargs -0 rm -f

dist:
	python setup.py bdist
	python setup.py bdist_egg
	python setup.py sdist

install:
	python setup.py install

.PHONY: commit update diff status test dist install
