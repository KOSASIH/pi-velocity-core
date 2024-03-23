from flask import make_response, jsonify, request

from src import app, db
from src.models import Block
from src.serializers import serialize, deserialize

@app.route('/')
def index():
    """
    Handles the root route

    Returns:
        str: A greeting message
    """

    return 'Hello, World!'

@app.route('/blocks', methods=['GET', 'POST'])
def blocks():
    """
    Handles the blocks route

    Args:
        methods (list): A list of HTTP methods

    Returns:
        str: A JSON-encoded string
    """

    if request.method == 'GET':
        blocks = Block.query.all()

        return serialize(blocks)

    if request.method == 'POST':
        data = request.json

        block = Block.create(data['data'])

        db.session.add(block)
        db.session.commit()

        return serialize(block), 201

@app.route('/blocks/<int:block_id>', methods=['PUT', 'DELETE'])
def block(block_id):
    """
    Handles the individual block route

    Args:
        block_id (int): The ID of the block

    Args:
        methods (list): A list of HTTP methods

    Returns:
        str: A JSON-encoded string
    """

    if request.method == 'PUT':
        data = request.json

        block = Block.query.get(block_id)

        block.data = data['data']

        db.session.commit()

        return serialize(block)

    if request.method == 'DELETE':
        block = Block.query.get(block_id)

        db.session.delete(block)
        db.session.commit()

        return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run()
