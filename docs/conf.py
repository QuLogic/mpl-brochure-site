import datetime
import subprocess

# -- Project information -----------------------------------------------------

html_title = 'Visualization with Python'
project = "Matplotlib landing page"
copyright = (
     f"© 2012 – {datetime.datetime.now().year} The Matplotlib development team"
 )
author = "Matplotlib Developers"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'notfound.extension',
    'sphinx_design',
]

# The language for content autogenerated by Sphinx. Refer to documentation for
# a list of supported languages.
language = 'en'

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_css_files = ['css/normalize.css', 'css/landing.css']
html_theme = "mpl_sphinx_theme"
html_favicon = "_static/favicon.ico"
html_theme_options = {
    "navbar_links": ("absolute", "server-stable"),
    "footer_start": ["landing_footer"],
    "secondary_sidebar_items": [],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the theme static files,
# so a file named "default.css" will overwrite the theme's "default.css".
html_static_path = ["_static"]

# Prefix added to all the URLs generated in the 404 page.
notfound_urls_prefix = '/'

# -- Options for sphinx-design ------------------------------------------------

sd_custom_directives = {
    "quicklink": {
        "inherit": "grid-item-card",
        "options": {
            "class-card": "sd-border-0",
            "class-img-top": "dark-light",
            "margin": "5",
            "shadow": "none",
            "text-align": "center",
        },
    }
}
