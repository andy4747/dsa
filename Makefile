.PHONY: test test-file test-function lint format clean install dev-install docs

# Run all tests
test:
	pytest -v

# Run tests in a specific file
# Usage: make test-file FILE=tests/test_leetcode/test_easy.py
test-file:
	pytest -v $(FILE)

# Run a specific test function
# Usage: make test-function FUNC=test_rotate_array
test-function:
	pytest -v -k "$(FUNC)"

# Run tests matching a keyword expression
# Usage: make test-k K="rotate or duplicate"
test-k:
	pytest -v -k "$(K)"

# Run tests with print statements
test-s:
	pytest -v -s

lint:
	flake8 src/ tests/
	mypy src/ tests/

format:
	black src/ tests/
	isort src/ tests/

docs:
	python scripts/generate_docs.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".tox" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +

install:
	pip install .

dev-install:
	pip install -e ".[test]"

uninstall:
	pip uninstall -y andy4747-dsa
	make clean