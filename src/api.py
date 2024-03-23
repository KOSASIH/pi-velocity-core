from flask_restful import Api, Resource, reqparse

from src.models import Block

class BlockListAPI(Resource):
    """
    Handles CRUD operations on Block objects
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        super().__init__()

    def get(self):
        """
        Get all blocks in the Blockchain

        Returns:
            list: A list of Block objects
        """

        blocks = Block.query.all()

        return blocks, 200

    def post(self):
        """
        Create a new Block

        Returns:
            Block: The newly created Block
        """

        # parse the request data
        self.reqparse.add_argument('data', type=str, help='No data in the request', required=True)

        data = self.reqparse.parse_args()

        # create a new Block
        block = Block.create(data=data['data'])

        return block, 201

block_parser = reqparse.RequestParser()

block_parser.add_argument('data', type=str, help='No data in the request', required=True)

class BlockAPI(Resource):
    """
    Handles CRUD operations on individual Block objects
    """

    def get(self, block_id):
        """
        Get a specific Block

        Args:
            block_id (int): The ID of the Block

        Returns:
            Block: The Block object
        """

        block = Block.query.filter_by(id=block_id).first()

        if block is None:
            return {'message': 'Block not found'}, 404

        return block, 200

    def put(self, block_id):
        """
        Update a specific Block

        Args:
            block_id (int): The ID of the Block

        Returns:
            Block: The updated Block
        """

        block = Block.query.filter_by(id=block_id).first()

        if block is None:
            return {'message': 'Block not found'}, 404

        # parse the request data
        self.reqparse.add_argument('data', type=str, help='No data in the request', required=True)

        data = self.reqparse.parse_args()

        block.data = data['data']

        return block, 200

    def delete(self, block_id):
        """
        Delete a specific Block

        Args:
            block_id (int): The ID of the Block

        Returns:
            dict: A success message
        """

        block = Block.query.filter_by(id=block_id).first()

        if block is None:
            return {'message': 'Block not found'}, 404

        block.delete()

        return {'message': 'Block deleted'}, 200

api = Api()

api.add_resource(BlockListAPI, '/blocks', endpoint='blocks')
api.add_resource(BlockAPI, '/blocks/<int:block_id>', endpoint='block')
