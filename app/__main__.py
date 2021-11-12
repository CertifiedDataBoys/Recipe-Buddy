from __init__ import create_app
from livereload import Server

# app is a Flask object
app = create_app()

# remember to use DEBUG mode for templates auto reload
# https://github.com/lepture/python-livereload/issues/144
app.debug = True

server = Server(app.wsgi_app)
# server.watch
server.serve()