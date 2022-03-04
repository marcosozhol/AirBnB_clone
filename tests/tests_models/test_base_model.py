#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Unittest for base model module.
This unittest is a collection of possible edge cases
on which this module should not be expected to fail,
and cases on which it is expected to fail.
"""

from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
import pep8
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """this will test the base model class"""

    def test_pep8_conformance_base_model(self):
        """pep8 test.
        This test is designed to make sure the Python code
        is up to the pep8 standard.
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_base_model_id_is_string(self):
        """UUID format testing.
        This test is designed to check if any generated UUID
        is correctly generated and has the propper format.
        """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_base_model_created_at_is_datetime(self):
        """Datetime test.
        This test is designed to check if the date and time in which a
        class was created are correctly assigned.
        """
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_base_model_updated_at_is_datetime(self):
        """Datetime test.
        This test is designed to check if the date and time in which a
        class is updated are correctly assigned.
        """
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)

    def test_method_BaseModel(self):
        """checking if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_to_dict_BaseModel(self):
        """test if to_dictionary method works"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    def test_save_BaseModel(self):
        """test if the save method works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_init_BaseModel(self):
        """test if the base is an instance of type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))


if __name__ == "__main__":
    unittest.main()
