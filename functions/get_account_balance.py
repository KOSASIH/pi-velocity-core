def get_account_balance(account_address):
    """
    Retrieves the balance of the specified account address.

    :param str account_address: the account address to retrieve the balance for
    :return: int, the account balance
    """

    # Look up the account in the blockchain
    account = get_account_from_blockchain(account_address)

    # Return the balance of the account
    return account['balance']
