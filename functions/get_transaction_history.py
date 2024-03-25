def get_transaction_history(user_address, pi_network):
    """
    Retrieve the transaction history of a user.

    :param user_address: The address of the user.
    :param pi_network: The Pi network object.
    :return: A list of transactions.
    """

    # Get all transactions associated with the user's address
    user_transactions = pi_network.get_transactions_by_address(user_address)

    # Filter out the incoming and outgoing transactions
    transaction_history = [
        t
        for t in user_transactions
        if user_address in (t["from"], t["to"])
    ]

    return transaction_history
