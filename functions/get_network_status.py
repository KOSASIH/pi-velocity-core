import requests

HORIZON_URL = "http://localhost:8000"

def get_network_status():
    """
    Retrieves the status of the Pi Network.
    """

    # Send a request to the local Horizon instance
    response = requests.get(f"{HORIZON_URL}/status")

    # Check if the request was successful
    if response.status_code == 200:

        # Extract the status data from the response
        network_status = response.json()["status"]

        # Return the status data
        return network_status

    # Return None if the request was not successful
    return None
