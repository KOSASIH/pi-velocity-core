import json
import unittest
from test.__init__ import TestCase


class TestViews(TestCase):
    def test_index(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_blocks(self):
        response = self.client.get("/blocks")

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)

        self.assertGreaterEqual(len(data), 1)

    def test_block(self):
        block = models.Block.create(data="Test Block")

        response = self.client.get(f"/blocks/{block.id}")

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)

        self.assertEqual(data["data"], "Test Block")

    def test_create_block(self):
        data = {"data": "Test Block"}

        response = self.client.post("/blocks", json=data)

        self.assertEqual(response.status_code, 201)

        data = json.loads(response.data)

        self.assertEqual(data["data"], "Test Block")

    def test_update_block(self):
        block = models.Block.create(data="Test Block")

        data = {"data": "New Test Block"}

        response = self.client.put(f"/blocks/{block.id}", json=data)

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)

        self.assertEqual(data["data"], "New Test Block")

    def test_delete_block(self):
        block = models.Block.create(data="Test Block")

        response = self.client.delete(f"/blocks/{block.id}")

        self.assertEqual(response.status_code, 200)

        response = self.client.get(f"/blocks/{block.id}")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
