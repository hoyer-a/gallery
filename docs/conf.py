# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

project = 'pyfar gallery'
copyright = '2024, The pyfar developers'
author = 'The pyfar developers'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx_gallery.load_style',
    'nbsphinx',
    'autodocsumm',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# default language for highlighting in source code
highlight_language = "python3"

# intersphinx mapping
intersphinx_mapping = {
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'spharpy': ('https://spharpy.readthedocs.io/en/stable/', None)
    }

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'insipid'
html_static_path = ['_static']


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'pyfar.tex',
     u'pyfar Gallery',
     u'The pyfar developers', 'manual'),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pyfar',
     u'pyfar Gallery',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pyfar',
     u'pyfar Gallery',
     author,
     'pyfar',
     'One line description of project.',
     'Miscellaneous'),
]

# -- Options for nbsphinx -------------------------------------------------
nbsphinx_prolog = r"""
{% set docname = 'doc/' + env.doc2path(env.docname, base=None) %}

.. raw:: html

    <div class="admonition note">
      Open an interactive online version by clicking the badge 
      <span style="white-space: nowrap;"><a href="https://mybinder.org/v2/gh/pyfar/pyfar_gallery/main?filepath={{ docname|e }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a></span>
      or
      <a href="{{ env.docname.split('/')|last|e + '.ipynb' }}" class="reference download internal" download>download</a>
      the notebook.
      <script>
        if (document.location.host) {
          let nbviewer_link = document.createElement('a');
          nbviewer_link.setAttribute('href',
            'https://nbviewer.org/url' +
            (window.location.protocol == 'https:' ? 's/' : '/') +
            window.location.host +
            window.location.pathname.slice(0, -4) +
            'ipynb');
          nbviewer_link.innerHTML = 'Or view it on <em>nbviewer</em>';
          nbviewer_link.classList.add('reference');
          nbviewer_link.classList.add('external');
          document.currentScript.replaceWith(nbviewer_link, '.');
        }
      </script>
    </div>

"""