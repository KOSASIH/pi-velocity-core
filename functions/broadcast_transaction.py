import hashlib
import json

def broadcast_transaction(transaction):
    """
    Broadcasts the given transaction to the Pi Network.

    Args:
        transaction (dict): The transaction to broadcast.

    Returns:
        bool: True if the transaction is successfully broadcasted, False otherwise.
    """

    # Serialize the transaction to JSON
    transaction_json = json.dumps(transaction)

    # Calculate the transaction hash
    transaction_hash = hashlib.sha256(transaction_json.encode()).hexdigest()

    # Broadcast the transaction to the network
    # TODO: Implement transmission details

    return True
