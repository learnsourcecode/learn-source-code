#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Vengat'
SITENAME = u'learnsourcecode'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS = None

TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_TAGS_ON_SIDEBAR = True

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/vengatlnx'),
          ('linkedin', 'https://in.linkedin.com/pub/vengatesh-selvaraj/83/8b1/446'),
          ('github', 'https://github.com/vengatlnx/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# path for theme directory
THEME = "theme"

# Boot strap theme
BOOTSTRAP_THEME = 'simplex'

BOOTSTRAP_NAVBAR_INVERSE = True
BANNER= 'images/palette.png'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

