import socket

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect_to_node(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send_to_node(self, message):
        self.socket.sendall(message.encode('utf-8'))

    def recv_from_node(self):
        return self.socket.recv(1024).decode('utf-8')

    def close_connection(self):
        self.socket.close()

class Network:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def send_messages_to_all_nodes(self, message):
        for node in self.nodes:
            node.send_to_node(message)

    def recv_messages_from_all_nodes(self):
        messages = []
        for node in self.nodes:
            message = node.recv_from_node()
            if message:
                messages.append(message)
        return messages

    def update_blockchain(self, new_chain):
        for node in self.nodes:
            node.send_to_node(new_chain)

    def connect_to_nodes(self):
        for node in self.nodes:
            node.connect_to_node()

    def close_connections(self):
        for node in self.nodes:
            node.close_connection()
