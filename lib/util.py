import hashlib
import base58

def hash_block(block):
    """
    Hashes a block using SHA-256.

    Args:
        block (Block): The block to hash.

    Returns:
        str: The hashed block.
    """
    block_string = str(block.index) + str(block.prev_hash) + str(block.timestamp) + str(block.data) + str(block.nonce)
    return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

def is_valid_proof(block, prev_block, difficulty):
    """
    Validates the proof of work for a block.

    Args:
        block (Block): The block to validate.
        prev_block (Block): The previous block.
        difficulty (int): The difficulty level.

    Returns:
        bool: True if the proof is valid, False otherwise.
    """
    prev_block_hash = prev_block.hash
    current_block_hash = hash_block(block)
    return current_block_hash.startswith('0' * difficulty) and prev_block_hash == block.prev_hash

def get_transaction_value(transaction):
    """
    Returns the value of a transaction.

    Args:
        transaction (Transaction): The transaction to get the value of.

    Returns:
        int: The value of the transaction.
    """
    return transaction.amount

def get_transaction_sender(transaction):
    """
    Returns the sender of a transaction.

    Args:
        transaction (Transaction): The transaction to get the sender of.

    Returns:
        str: The sender of the transaction.
    """
    return transaction.sender

def get_transaction_receiver(transaction):
    """
    Returns the receiver of a transaction.

    Args:
        transaction (Transaction): The transaction to get the receiver of.

    Returns:
        str: The receiver of the transaction.
    """
   return transaction.receiver

def encode_base58(bytes_string):
    """
    Encodes a byte string in base58 format.

    Args:
        bytes_string (bytes): The byte string to encode.

    Returns:
        str: The encoded base58 string.
    """
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    b58 = b""

    for byte in bytes_string:
        coeff = 0
        for char in alphabet:
            if byte == (pow(58, coeff) * int(char, 16)):
                b58 += bytes(char, encoding='utf8')
                break
            coeff += 1

    return b58.decode('utf-8')

def decode_base58(base58_string):
    """
    Decodes a base58 string to a byte string.

    Args:
        base58_string (str): The base58 string to decode.

    Returns:
        bytes: The decoded byte string.
    """
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    bytes_string = b""

    for char in base58_string:
        if char not in alphabet:
            raise ValueError("Invalid base58 string.")
        coeff = 0
        for i in range(39, -1, -1):
            if alphabet[i] == char:
                bytes_string += pow(58, coeff, 256)
                break
            coeff += 1

    return bytes_string

def validate_address(address):
    if address is None:
        return False

    try:
        decode_base58(address)
    except ValueError:
        return False

    return True
