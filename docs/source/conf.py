# Configuration file for the Sphinx documentation builder.

import io
import os

# Derive the navy PDF cover logo from the white HTML SVG at build time, so only
# the SVG is a committed source asset (needs cairosvg + Pillow, both in
# requirements.txt).
try:
    import cairosvg
    from PIL import Image
except ImportError as e:
    raise RuntimeError(
        "The docs build needs cairosvg and Pillow to generate the PDF cover logo; "
        "install them with: pip install -r requirements.txt"
    ) from e

_static = os.path.join(os.path.dirname(__file__), '_static')
with open(os.path.join(_static, 'cryptnox-logo.svg'), encoding='utf-8') as f:
    _svg = f.read()
_png = cairosvg.svg2png(
    bytestring=_svg.replace('fill="white"', 'fill="#101f2e"').encode(),
    output_width=1200, output_height=226,
)
Image.open(io.BytesIO(_png)).save(
    os.path.join(_static, 'cryptnox-logo-dark.png'), dpi=(400, 400)
)

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
# Built by CI with pdflatex; same cover and page layout as the cryptnox-cli
# manual. Output: cryptnox-readers.pdf

latex_engine = 'pdflatex'
latex_logo = '_static/cryptnox-logo-dark.png'  # generated above; the white logo is invisible on the white cover
latex_documents = [
    ('index', 'cryptnox-readers.tex', 'Cryptnox Smart Card Readers Manual', author, 'manual'),
]
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'figure_align': 'H',
    'sphinxsetup': 'pre_border-radius=0pt',  # sharp rectangle corners on code-block frames
    'extraclassoptions': 'oneside,openany',  # no blank filler pages (web PDF)
    'printindex': '',  # no general Index in the PDF
    'fncychap': '',  # no fancy chapter rules; titlesec styles chapters instead
    'preamble': r'''
% pdflatex has no glyphs for the ✅/❌ marks used in the compatibility tables;
% map them to pifont's check and cross
\usepackage{pifont}
\DeclareUnicodeCharacter{2705}{\ding{51}}
\DeclareUnicodeCharacter{274C}{\ding{55}}
% Literals (\ttfamily) in Inconsolata
\usepackage{inconsolata}
% Left-align body text (ragged right instead of justified)
\usepackage[document]{ragged2e}
% Drop the "(continues on next page)" / "(continued from previous page)" labels on code blocks
\AtBeginDocument{\renewcommand*\sphinxstylecodecontinued[1]{}\renewcommand*\sphinxstylecodecontinues[1]{}}
% Whole document in the sans font (TeX Gyre Heros)
\renewcommand{\familydefault}{\sfdefault}
% Sans-serif TOC entries
\AtBeginDocument{\addtocontents{toc}{\protect\sffamily}}
% Left-aligned chapter headings
\usepackage{titlesec}
\titleformat{\chapter}[hang]{\sffamily\bfseries\huge}{\thechapter}{1em}{}
\titlespacing*{\chapter}{0pt}{0pt}{20pt}
% Centered page header (manual title) + copyright footer
\usepackage{fancyhdr}
\def\headruleskip{4pt}\def\footruleskip{4pt}% gap between header/footer text and rule
\AtBeginDocument{%
  \fancypagestyle{normal}{%
    \fancyhf{}%
    \fancyhead[C]{\sffamily\nouppercase{Cryptnox Smart Card Readers Manual}}%
    \fancyfoot[L]{\sffamily\copyright{} 2026 Cryptnox SA}%
    \fancyfoot[R]{\sffamily\thepage}%
    \renewcommand{\headrulewidth}{0.4pt}%
    \renewcommand{\footrulewidth}{0.4pt}%
  }%
  \fancypagestyle{plain}{%
    \fancyhf{}%
    \fancyfoot[L]{\sffamily\copyright{} 2026 Cryptnox SA}%
    \fancyfoot[R]{\sffamily\thepage}%
    \renewcommand{\headrulewidth}{0pt}%
    \renewcommand{\footrulewidth}{0.4pt}%
  }%
  \pagestyle{normal}%
}
% Cover page: logo, title, release and date; no author line (the logo brands it)
\makeatletter
\renewcommand{\sphinxmaketitle}{%
  \let\sphinxrestorepageanchorsetting\relax
  \ifHy@pageanchor\def\sphinxrestorepageanchorsetting{\Hy@pageanchortrue}\fi
  \hypersetup{pageanchor=false}%
  \begin{titlepage}%
    \let\footnotesize\small \let\footnoterule\relax
    \begingroup
      \def\endgraf{ }\def\and{\& }%
      \pdfstringdefDisableCommands{\def\\{, }}%
      \hypersetup{pdfauthor={\@author}, pdftitle={\@title}}%
    \endgroup
    \noindent\rule{\textwidth}{1pt}\par
    \begin{flushright}%
      \vskip 1em%
      \includegraphics[width=7cm]{cryptnox-logo-dark}\par
      \vskip 2em%
      {\LARGE\py@HeaderFamily \@title \par}%
      \vskip 0.5em%
      {\large\itshape \py@release\releaseinfo \par}%
      \vfill
      {\large \@date \par}%
    \end{flushright}%
    \@thanks
  \end{titlepage}%
  \setcounter{footnote}{0}%
  \let\thanks\relax\let\maketitle\relax
  \clearpage
  \ifdefined\sphinxbackoftitlepage\sphinxbackoftitlepage\fi
  \if@openright\cleardoublepage\else\clearpage\fi
  \sphinxrestorepageanchorsetting
}
\makeatother
''',
}
