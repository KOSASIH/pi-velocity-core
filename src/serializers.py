from marshmallow import Schema, fields

class BlockSchema(Schema):
    """
    Serializes and deserializes Block objects

    Attributes:
        id (int): The ID of the Block
        data (str): The data stored in the Block
        timestamp (datetime): The timestamp of the Block
    """

    id = fields.Int(dump_only=True)
    data = fields.Str(required=True)
    timestamp = fields.DateTime(dump_only=True)

    class Meta:
        """
        Configures the serializer

        Attributes:
            unknown (EXCLUDE): Excludes any unknown fields during deserialization
        """

        unknown = EXCLUDE

block_schema = BlockSchema()
blocks_schema = BlockSchema(many=True)

def serialize(data: dict):
    """
    Serializes a dictionary

    Args:
        data (dict): A dictionary to serialize

    Returns:
        str: A JSON-encoded string of the serialized data
    """

    return block_schema.jsonify(data)

def deserialize(data: str):
    """
    Deserializes a JSON-encoded string

    Args:
        data (str): A JSON-encoded string to deserialize

    Returns:
        dict: The deserialized dictionary
    """

    return block_schema.load(data)

def serialize_list(data: list):
    """
    Serializes a list of dictionaries

    Args:
        data (list): A list of dictionaries to serialize

    Returns:
        str: A JSON-encoded string of the serialized list of dictionaries
    """

    return blocks_schema.jsonify(data)

def deserialize_list(data: str):
    """
    Deserializes a JSON-encoded string of a list of dictionaries

    Args:
        data (str): A JSON-encoded string to deserialize

    Returns:
        list: The deserialized list of dictionaries
    """

   return blocks_schema.load(data)
