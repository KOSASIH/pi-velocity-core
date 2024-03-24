def handle_outgoing_connections(peer_list):
    """
    Handles outgoing connections to other nodes in the network.

    :param peer_list: A list of peer addresses to connect to.

    """

    # Loop through the list of peer addresses
    for peer in peer_list:
        # Create a new socket for the outgoing connection
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the connection attempt
        connection.settimeout(5.0)

        try:
            # Connect to the peer
            connection.connect(peer)

            # Log the successful connection
            print(f"Connected to peer {peer}")

            # Start a new thread for handling the outgoing connection
            thread = threading.Thread(
                target=handle_client_connection, args=(connection,)
            )
            thread.start()

        except Exception as e:
            print(f"Error connecting to peer {peer}: {e}")

            # Close the connection
            connection.close()
