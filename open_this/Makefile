install:
	python3 -m venv venv
	./venv/bin/pip install build
	./venv/bin/python3 -m build --wheel
	cp dist/mazegen-*.whl .
	./venv/bin/pip install dist/mazegen-*.whl --force-reinstall
	./venv/bin/pip install mlx-*.whl

run:
	./venv/bin/python3 a_maze_ing.py config.txt

debug:
	./venv/bin/python -m pdb a_maze_ing.py config.txt

clean:
	rm -rf __pycache__ .mypy_cache *.pyc
	rm -rf build/
	rm -rf dist/
	rm -rf mazegen.egg-info/
	rm -f mazegen-*.whl

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

.PHONY: install run debug clean lint lint-strict
