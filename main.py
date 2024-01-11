import socketserver
import threading
import socket




class ProxyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        request_data = self.request.recv(1024)
        print(f"Request:\n{request_data.decode('utf-8')}")

        # Forward the request to the target server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.connect(('127.0.0.1', 9001))
            server_socket.sendall(request_data)

            # Receive the server's response
            response_data = server_socket.recv(4096)
            print(f"Received response:\n{response_data.decode('utf-8')}")

            # You can inspect and manipulate the response_data here

            # Forward the response to the client
            self.request.sendall(response_data)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def main():
    host, port = '127.0.0.1', 8081
    server = ThreadedTCPServer((host, port), ProxyHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    print(f"Proxy listening on {host}:{port}...")

    try:
        server_thread.join()
    except KeyboardInterrupt:
        print("Proxy server shutting down.")
        server.shutdown()

if __name__ == "__main__":
    main()
