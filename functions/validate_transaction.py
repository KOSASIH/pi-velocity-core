def validate_transaction(transaction, network):
    """
    Validates the transaction inputs and outputs for pi-velocity-core network.
    :param transaction: The transaction object to validate.
    :param network: The pi-velocity-core network object.
    :return: True if the transaction is valid, False otherwise.
    """

    # Check if transaction is null or empty
    if transaction is None or len(transaction) == 0:
        return False

    # Check if transaction fields are valid
    if 'id' not in transaction or transaction['id'] is None or len(transaction['id']) == 0:
        return False
    if 'sender' not in transaction or transaction['sender'] is None or len(transaction['sender']) == 0:
        return False
    if 'receiver' not in transaction or transaction['receiver'] is None or len(transaction['receiver']) == 0:
        return False
    if 'amount' not in transaction or transaction['amount'] is None:
        return False
    if 'fee' not in transaction or transaction['fee'] is None:
        return False

    # Check if transaction inputs and outputs are valid
    sender = network.get_account(transaction['sender'])
    if sender is None or sender.balance < transaction['amount'] + transaction['fee']:
        return False

    receiver = network.get_account(transaction['receiver'])
    if receiver is None:
        return False

    return True
