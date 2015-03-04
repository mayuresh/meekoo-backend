__author__ = 'mayureshp'

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os

from hello import app

PORT = 5000
if os.environ["PORT"]:
    PORT = int(os.environ["PORT"])

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(PORT)
IOLoop.instance().start()