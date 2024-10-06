import os
import subprocess

def generate_docs():
    # Change to the project root directory
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Generate RST files
    subprocess.run(['python', 'scripts/generate_rst_files.py'])

    # Build the documentation
    subprocess.run(['sphinx-build', '-b', 'html', 'docs', 'docs/_build'])

    print("Documentation generated. Open docs/_build/index.html to view.")

if __name__ == "__main__":
    generate_docs()
