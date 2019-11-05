#! /usr/bin/env python3
# coding: UTF-8

""" Class TestCallApi """

# import
from unittest import TestCase
from unittest.mock import patch
from purbeurre.food.classes.call_api import CallApi




class TestCallApi(TestCase):

    def setUp(self):
        self.new_call_api = CallApi()

    @patch('purbeurre.food.classes.call_api.requests.get')
    def test_return_request(self, mock_api):

        result_json = [{'page': '1', 'count': 0, 'skip': 0, 'page_size': '100', 'products': []},
                       {'page': '1', 'count': 0, 'skip': 0, 'page_size': '100', 'products': []},
                       {'products': [], 'page_size': '100', 'skip': 0, 'count': 0, 'page': '1'},
                       {'page': '1', 'count': 0, 'skip': 0, 'page_size': '100', 'products': []},
                       {'skip': 0, 'count': 8, 'page': '1', 'products': ['data'], 'page_size': '100'}]

        mock_api.return_value.json.return_value = result_json

        categories_list = ["pizza"]

        self.assertEqual(self.new_call_api.load_data(categories_list), result_json)
