from datetime import datetime

import pytest

import models

def test_create_block():
    """
    Test creating a new block
    """

    block = models.Block.create(data='Test Block')

    assert block.id is not None
    assert block.data == 'Test Block'
    assert block.timestamp is not None

def test_block_eq():
    """
    Test block equality
    """

    block1 = models.Block.create(data='Test Block 1')
    block2 = models.Block.create(data='Test Block 1')

    assert block1 == block2

def test_block_ne():
    """
    Test block inequality
    """

    block1 = models.Block.create(data='Test Block 1')
    block2 = models.Block.create(data='Test Block 2')

    assert block1 != block2

def test_block_gte():
    """
    Test block timestamp is greater than or equal to
    """

    block1 = models.Block(data='Test Block', timestamp=datetime.utcnow())
    block2 = models.Block.create(data='Test Block')

    assert block1.timestamp >= block2.timestamp

def test_block_lte():
    """
    Test block timestamp is less than or equal to
    """

    block1 = models.Block(data='Test Block', timestamp=datetime.utcnow())
    block2 = models.Block.create(data='Test Block')

    assert block1.timestamp <= block2.timestamp

def
