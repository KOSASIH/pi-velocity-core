import socket
import ssl


def secure_communication(host, port, certfile, keyfile, timeout=None):
    """
    Establish a secure communication channel with a remote server.

    Args:
        host (str): The remote host to connect to.
        port (int): The remote port to connect to.
        certfile (str): The path to the SSL certificate file.
        keyfile (str): The path to the SSL key file.
        timeout (float): The timeout value for the socket.

    Returns:
        A secure socket connection.

    Raises:
        SSLCertificateError: If the SSL certificate cannot be verified.
        TimeoutError: If the socket times out.
    """

    # Create a context with the SSL certificate and key
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile, keyfile)

    # Connect to the remote host
    sock = socket.create_connection((host, port))

    # Create a socket wrapper with SSL
    wrapped_sock = context.wrap_socket(sock, server_hostname=host)

    # Set the timeout
    if timeout is not None:
        wrapped_sock.settimeout(timeout)

    # Return the secure socket
    return wrapped_sock
