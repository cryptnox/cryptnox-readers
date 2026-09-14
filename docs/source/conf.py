# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Cryptnox Smart Card Readers'
copyright = '2026, Cryptnox SA'
author = 'Cryptnox'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = ['sphinx_sitemap']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- SEO meta tags -----------------------------------------------------------

html_baseurl = 'https://docs.cryptnox.com/cryptnox-readers/'
html_title = 'Cryptnox Smart Card Readers'
sitemap_url_scheme = "{link}"

html_meta = {
    'description': 'Compatibility documentation for Cryptnox USB smart card readers: '
                   'national eID and professional cards by country, and FIDO2 services '
                   'and platforms.',
    'keywords': 'Cryptnox, smart card reader, USB-C, CCID, PC/SC, eID, FIDO2, NFC, '
                'ISO 7816, ISO 14443, extended APDU, documentation',
    'author': 'Cryptnox',
    'robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large',
}

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_last_updated_fmt = '%Y-%m-%d'  # visible page dates — AI answers prefer dateable sources
html_logo = '_static/cryptnox-logo.svg'
html_favicon = '_static/favicon.png'

html_css_files = [
    'custom.css',
]

html_theme_options = {
    'analytics_id': 'GT-PJ7HDFB',
    'logo_only': False,
    'prev_next_buttons_location': 'none',
    'style_external_links': False,
    'style_nav_header_background': '#101f2e',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 2,
    'includehidden': True,
    'titles_only': False,
}

html_show_sourcelink = False
html_copy_source = False
html_show_sphinx = False

# -- Options for PDF (LaTeX) output ------------------------------------------

latex_engine = 'pdflatex'
latex_documents = [
    ('index', 'cryptnox-readers.tex', 'Cryptnox Smart Card Readers',
     'Cryptnox SA', 'manual'),
]
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    # pdflatex has no glyphs for the ✅/❌ marks used in the compatibility
    # tables; map them to pifont's check and cross so the PDF builds.
    'preamble': r'''
\usepackage{pifont}
\DeclareUnicodeCharacter{2705}{\ding{51}}
\DeclareUnicodeCharacter{274C}{\ding{55}}
''',
}
