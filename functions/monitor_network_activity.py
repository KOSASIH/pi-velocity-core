import time

class Network:
    def __init__(self):
        self.status = "idle"

    def monitor_network_activity(self):
        """
        Monitors the activity in the network and updates the node's status accordingly.
        """
        while True:
            time.sleep(5)  # check the network activity every 5 seconds
            if self.is_network_active():
                self.status = "active"
            else:
                self.status = "idle"

    def is_network_active(self):
        """
        Checks if the network is active.
        Returns:
            bool: True if the network is active, False otherwise.
        """
        # Implement your own logic to check if the network is active.
        # For example, you can check if there is any incoming or outgoing connections.
        pass
