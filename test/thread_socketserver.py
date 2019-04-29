import errno
import socket
import threading
import time

EOL1 = b'\r\n'
EOL2 = b'\r\n'
body = '''hello,world!<h1>from the5fire 《django企业开发实战》</h1> - from {thread_name}'''
response_params = {
    "HTTP/1.0 200 ok",
    "Date:sun 27 may 2018 01:01:01 GMT",

}
