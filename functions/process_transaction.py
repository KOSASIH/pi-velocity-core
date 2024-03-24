def process_transaction(transaction, network):
    """
    Processes a transaction and updates the network.
    :param transaction: The transaction object.
    :param network: The Pi Network object.
    :return: True if the transaction is processed successfully, False otherwise.
    """
    # Validate the transaction
    if not validate_transaction(transaction):
        print("Error: The transaction is invalid.")
        return False

    # Check if the sender has enough balance
    sender = network.get_account(transaction['sender'])
    if sender.balance < transaction['amount'] + transaction['fee']:
        print("Error: The sender has insufficient balance.")
        return False

    # Process the transaction
    sender.balance -= transaction['amount'] + transaction['fee']
    receiver = network.get_account(transaction['receiver'])
    receiver.balance += transaction['amount']
    network.add_transaction(transaction)

    # Add the transaction fee to the miner's reward
    miner = network.get_miner()
    miner.reward += transaction['fee']

    # Broadcast the transaction to the network
    network.broadcast_transaction(transaction)

    return True
