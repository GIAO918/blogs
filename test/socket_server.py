import socket

EOL1 = b"\n\n"
EOL2 = b"\n\r\n"
body = '''hello,world !<h1> from the5fire 《django企业开发实战》</h1>'''

response_params = [
    "HTTP/1.0 200 OK",
    "Date: sun,27 may 2018 01:01:01 GMT",
    "Content-Type: text/html;charset=utf-8",
    "Content-length:{}\r\n".format(len(body.encode())),
    body,
]
response = "\r\n".join(response_params)


def handle_connection(conn, addr):
    print("oh,new conn",conn,addr)
    import time
    time.sleep(10)
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    conn.send(response.encode())
    conn.close()


def main():
    socket.AF_INET
    socket.SOCK_STREAM
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(("127.0.0.1",8000))
    serversocket.listen(5)
    print("http://127.0.0.1:8000")

    try:
        while True:
            conn, address = serversocket.accept()
            handle_connection(conn, address)
    finally:
        serversocket.close()


if __name__ == "__main__":
    main()
