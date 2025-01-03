# Configuration file for the Sphinx documentation builder.
import os
import sys
from sphinx.util import logging

log = logging.getLogger('sphinx.conf')

module_path = os.path.realpath("./../../")
sys.path.append(module_path)
log.info("Added path %s to sys.path", module_path)

# -- Project information

project = 'RTD Test'
copyright = '2024, FeRD'
author = 'ferdnyc@gmail.com'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_build_compatibility.extension',
    'sphinx_autorun',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'furo'

# -- Options for EPUB output
epub_show_urls = 'footnote'
