#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jason'
SITENAME = 'Jason Figueroa'
# SITEURL = 'http://localhost:8000'
# ABOUTURL = 'http://localhost:8000/pages/about-me.html'
# ABOUTSITEURL = 'http://localhost:8000/pages/about-site.html'
SITEURL = 'https://jasonfigueroa.github.io'
ABOUTURL = 'https://jasonfigueroa.github.io/pages/about-me.html'
ABOUTSITEURL = 'https://jasonfigueroa.github.io/pages/about-site.html'

THEME = 'pelican-blue'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# added for pelican-blue theme
SIDEBAR_DIGEST = 'Passionate Learner'

# FAVICON = 'http://localhost:8000/images/favicon.ico'
FAVICON = 'https://jasonfigueroa.github.io/images/favicon.ico'

DISPLAY_PAGES_ON_MENU = True

# TWITTER_USERNAME = 'jasonfigueroa_'

MENUITEMS = (('Blog', SITEURL), ('About Me', ABOUTURL), ('About This Site', ABOUTSITEURL))
# end

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('talkpython', 'https://talkpython.fm/'),
#          ('awesome-python', 'https://awesome-python.com/'),
#          ('full stack python', 'https://www.fullstackpython.com/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/jasonfigueroa_'),
          ('github', 'https://github.com/jasonfigueroa'),
          ('linkedin', 'https://www.linkedin.com/in/jason-figueroa-b59a3798/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

DISQUS_SITENAME = "jasonfigueroa"
