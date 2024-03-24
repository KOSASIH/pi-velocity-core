def start_transaction():
    """
    Initiates a new transaction.
    """
    # Create a new transaction object
    transaction = {
        "id": str(uuid.uuid4()),
        "sender": None,
        "receiver": None,
        "amount": None,
        "fee": None,
        "timestamp": datetime.datetime.now(),
    }
    return transaction
