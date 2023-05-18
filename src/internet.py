import socket

class Internet():

    is_available: bool = False
    
    def __init__():
        pass

    def check_connectivity(self):
        try:
            host = '8.8.8.8'
            port = '443'
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(7)
            sock.connect('8.8.8.8', '443')
            print(f"Connected to {host} on port {port}")
            sock.close()
            self.is_available = True
        except socket.error:
            print(f"Unable to connect to {host} on port {port}")