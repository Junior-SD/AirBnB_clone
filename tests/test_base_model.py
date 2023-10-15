#!/usr/bin/python3
""" File containing tests done for base_model.py
"""


import unittest
import uuid
import models
from datetime import datetime
class Test_BaseModel(unittest.TestCase):
    """ Test cases of the base_model.py file """
    def setUp(self):
        """ Method called to prepare the test fixture i.e
        create an instance of the BaseModel class
        """
        obj = BaseModel()

    def test_init(self):
        """Tests the __init__()"""
        # check if the id attribute uses the UUID string
        self.assertTrue(uuid.UUID(obj.id, version=4))

        # check if 'created_at' anf 'updated_at' uses the datetime format
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str():
        """Test the __str()"""
        expectedstring = f"[{BaseModel.__name__}] ({self.obj.id}) {self.obj.__dict__}}"
        self.assertEqual(str(self.obj), expectedstring)

    def test_save(self):
        """ Test the save function """
        self.obj.save()

        # check if the updated_at attribute is of the current time
        self.assertTrue(self.obj.updated_at > datetime.now())

        # call the save method
        # self.obj.save()

    def tes_to_dict(self):
        obj_dict = self.obj.to_dict()

        # ensure the dictionary has the expected keys
        self.assertIn("id", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)
        self.assertIn("__class__", obj_dict)

        # check that the created_at and updated_at attributes use the ISO Format
        self.assertTrue(isinstance(datetime.fromisoformat(obj_dict["created_at"]), datetime))
         self.assertTrue(isinstance(datetime.fromisoformat(obj_dict["updated_at"]), datetime))

if __name__ = "__main__":
    unittest.main()
