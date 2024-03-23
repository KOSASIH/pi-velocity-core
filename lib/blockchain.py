import hashlib
import time

from lib.util import to_binary

class Block:
    def __init__(self, index, prev_hash, timestamp, data, hash, difficulty):
        self.index = index
        self.prev_hash = prev_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.difficulty = difficulty

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0" * 64, int(time.time()), "Genesis Block", "0" * 64, 4)

    def get_latest_block(self):
        return self.chain[-1]

    def add_new_block(self, data):
        prev_block = self.get_latest_block()
        new_block = Block(prev_block.index + 1, prev_block.hash, int(time.time()), data, None, prev_block.difficulty)
        new_block.hash = self.calculate_hash_for_block(new_block)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]

            if current_block.hash != self.calculate_hash_for_block(current_block):
                return False

            if current_block.difficulty > prev_block.difficulty:
                return False

            if current_block.difficulty < self.target_difficulty:
                current_block.difficulty = self.target_difficulty

        return True

    def calculate_hash_for_block(self, block):
        block_string = to_binary(block.index) + to_binary(block.prev_hash) + to_binary(block.timestamp) + to_binary(block.data) + to_binary(block.difficulty)
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

    @property
    def target_difficulty(self):
        return 2 ** (64 - 4)
