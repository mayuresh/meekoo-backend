__author__ = 'mayureshp'

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os

from api.main import app

PORT = 5000
if "PORT" in os.environ.keys():
    PORT = int(os.environ["PORT"])

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(PORT)
print("Server started on port %s" % (PORT))
IOLoop.instance().start()