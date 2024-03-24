def handle_incoming_connections(listener):
    """
    Handles incoming connections from other nodes in the network.

    :param listener: A listener object for accepting incoming connections.

    """

    # Loop forever to handle incoming connections
    while True:
        # Wait for a new connection to be established
        connection, address = listener.accept()

        # Log the incoming connection
        print(f"Accepted connection from {address}")

        # Start a new thread for handling the incoming connection
        thread = threading.Thread(target=handle_client_connection, args=(connection,))
        thread.start()


def handle_client_connection(connection):
    """
    Handles a single incoming connection from a client.

    :param connection: A socket object for the incoming connection.

    """

    # Loop until the connection is closed
    while True:
        try:
            # Receive data from the client
            data = connection.recv(BUFF_SIZE)

            # Check if the connection has been closed
            if not data:
                break

            # Parse the received data
            message = json.loads(data.decode())

            # Handle the received message
            handle_message(message)

        except Exception as e:
            print(f"Error handling client connection: {e}")

            # Close the connection
            connection.close()

            break
