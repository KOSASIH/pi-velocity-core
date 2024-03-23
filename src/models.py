import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Block(Base):
    """
    A Block represents a block in the Blockchain

    Attributes:
        id (int): The ID of the block
        data (str): The data stored in the block
        timestamp (datetime): The timestamp of the block creation
    """

    __tablename__ = "blocks"

    id = Column(Integer, primary_key=True)
    data = Column(String(255), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        """
        Returns a string representation of the object

        Returns:
            str: A string representation of the object
        """

        return f"Block(id={self.id}, data={self.data}, timestamp={self.timestamp})"

    def __init__(self, data: str):
        """
        Initializes the Block object

        Args:
            data (str): The data to be stored in the block
        """

        self.data = data

    @staticmethod
    def create(data: str):
        """
        Creates a new Block

        Args:
            data (str): The data to be stored in the block

        Returns:
            Block: The newly created Block
        """

        block = Block(data=data)

        return block

    def to_dict(self):
        """
        Converts the object to a dictionary

        Returns:
            dict: The object as a dictionary
        """

        return {
            "id": self.id,
            "data": self.data,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Creates a Block object from a dictionary

        Args:
            data (dict): A dictionary to create the Block objectfrom

        Returns:
            Block: A Block object created from the dictionary
        """

        block = Block(
            data=data.get("data"),
            timestamp=data.get("timestamp")
        )

        block.id = data.get("id")

        return block

    def delete(self):
        """
        Deletes the object from the database
        """

        from src import db

        db.session.delete(self)
        db.session.commit()
