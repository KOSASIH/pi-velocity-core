def add_block_to_chain(block, chain):
    """
    Adds the validated block to the blockchain.

    Args:
        block (dict): The block to be added.
        chain (list): The current blockchain.

    Returns:
        list: The updated blockchain.
    """

    # Add the block to the blockchain
    chain.append(block)

    return chain
