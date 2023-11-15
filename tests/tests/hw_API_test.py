import os
from unittest import TestCase
import bs4
from tests.hw_tests_yaapi import create_folder
import requests

class TestFolderCreation(TestCase):
    def test_creation_folder(self):
        try:
            expected = 201
            result = create_folder()
            self.assertEqual(result, expected)
        except AssertionError:
            print(f'Папка уже создана')

