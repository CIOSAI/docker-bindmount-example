#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

PORT = 5379


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print("Serving HTTP on port", PORT, "...")
    httpd.serve_forever()


run()
