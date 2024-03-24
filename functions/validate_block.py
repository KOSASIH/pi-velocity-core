def validate_block(block):
    """
    Validates the block headers and transactions.

    Args:
        block (dict): The block to be validated.

    Returns:
        bool: True if the block is valid, False otherwise.
    """

    # Check if the block headers are valid
    if not validate_block_headers(block):
        return False

    # Check if the block transactions are valid
    if not validate_block_transactions(block):
        return False

    return True
