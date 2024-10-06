import os
import shutil

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path, content=''):
    with open(path, 'w') as f:
        f.write(content)

def generate_project_structure():
    # Define the project root
    root = 'dsa_project'

    # Create the main project directory
    create_directory(root)

    # Create src directory and its subdirectories
    src_dirs = [
        'data_structures',
        'algorithms',
        'leetcode/easy',
        'leetcode/medium',
        'leetcode/hard',
        'neetcode/arrays_and_hashing',
        'neetcode/two_pointers',
        'neetcode/sliding_window',
        'neetcode/stack',
        'neetcode/binary_search',
        'neetcode/linked_list',
        'neetcode/trees',
        'neetcode/tries',
        'neetcode/heap_priority_queue',
        'neetcode/backtracking',
        'neetcode/graphs',
        'neetcode/advanced_graphs',
        'neetcode/1d_dynamic_programming',
        'neetcode/2d_dynamic_programming',
        'neetcode/greedy',
        'neetcode/intervals',
        'neetcode/math_and_geometry',
        'neetcode/bit_manipulation'
    ]

    for dir in src_dirs:
        create_directory(os.path.join(root, 'src', dir))
        create_file(os.path.join(root, 'src', dir, '__init__.py'))

    # Create some example files in src
    create_file(os.path.join(root, 'src', 'data_structures', 'linked_list.py'))
    create_file(os.path.join(root, 'src', 'data_structures', 'stack.py'))
    create_file(os.path.join(root, 'src', 'data_structures', 'tree.py'))
    create_file(os.path.join(root, 'src', 'algorithms', 'sorting.py'))
    create_file(os.path.join(root, 'src', 'algorithms', 'searching.py'))

    # Create tests directory and subdirectories
    test_dirs = ['test_data_structures', 'test_algorithms', 'test_leetcode', 'test_neetcode']
    for dir in test_dirs:
        create_directory(os.path.join(root, 'tests', dir))
    create_file(os.path.join(root, 'tests', '__init__.py'))

    # Create docs directory
    create_directory(os.path.join(root, 'docs', 'api'))
    create_file(os.path.join(root, 'docs', 'conf.py'))
    create_file(os.path.join(root, 'docs', 'index.rst'))

    # Create scripts directory
    create_directory(os.path.join(root, 'scripts'))
    create_file(os.path.join(root, 'scripts', 'run_tests.sh'), '#!/bin/bash\npytest')
    create_file(os.path.join(root, 'scripts', 'generate_docs.sh'), '#!/bin/bash\nsphinx-build docs docs/_build')

    # Create notebooks directory
    create_directory(os.path.join(root, 'notebooks'))
    create_file(os.path.join(root, 'notebooks', 'algorithm_analysis.ipynb'))

    # Create root level files
    create_file(os.path.join(root, 'requirements.txt'), 'pytest\nsphinx\njupyter\ntox')
    create_file(os.path.join(root, 'setup.py'), '''
from setuptools import setup, find_packages

setup(
    name="dsa_project",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest",
        "sphinx",
        "jupyter",
        "tox",
    ],
)
''')
    create_file(os.path.join(root, 'README.md'), '# DSA Project\n\nThis project contains implementations of various data structures and algorithms, as well as solutions to problems from LeetCode and the NeetCode roadmap.')
    create_file(os.path.join(root, '.gitignore'), '''
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
env/

# IDE files
.vscode/
.idea/

# Jupyter Notebook
.ipynb_checkpoints

# Distribution / packaging
dist/
build/
*.egg-info/

# Unit test / coverage reports
htmlcov/
.coverage
.tox/

# Sphinx documentation
docs/_build/
''')
    create_file(os.path.join(root, 'tox.ini'), '''
[tox]
envlist = py38, py39, py310
isolated_build = true

[testenv]
deps = pytest
commands =
    pytest tests
''')

    print(f"Project structure created in '{root}' directory.")

if __name__ == "__main__":
    generate_project_structure()
