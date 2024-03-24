def verify_block_signature(block, signature):
    """
    Verifies the block signature.

    Args:
        block (dict): The block to be verified.
        signature (str): The block signature.

    Returns:
        bool: True if the block signature is valid, False otherwise.
    """

    # Serialize the block
    block_data = json.dumps(block)

    # Verify the block signature using the block data and public key
    public_key = get_block_author_public_key(block)
    return verify_signature(public_key, signature, block_data)
