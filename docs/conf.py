import os
import sys

# -- Project information -----------------------------------------------------
project = 'andy4747/dsa'
copyright = '2024, Angel Dhakal'
author = 'Angel Dhakal'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',          # Automatically extract docstrings
    'sphinx.ext.napoleon',         # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',         # Add links to highlighted source code
    'sphinx.ext.intersphinx',      # Link to other project's documentation
    'sphinx_autodoc_typehints',    # Support for Python type annotations
    'sphinx.ext.todo',             # Support for TODO items
    'myst_parser',                 # Support for Markdown
    'sphinx_copybutton',           # Add copy button to code blocks
]

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_book_theme'
html_theme_options = {
    "repository_url": "https://github.com/andy4747/dsa",
    "repository_branch": "master",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_download_button": True,
    "use_fullscreen_button": True,
    "use_sidenotes": True,
    "show_toc_level": 2,
}

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath('..'))

# -- Napoleon settings ------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# -- Autodoc settings ------------------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# -- Intersphinx settings -------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- MyST settings -------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
