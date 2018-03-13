# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.update_model_response import UpdateModelResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestModelsController(BaseTestCase):
    """ModelsController integration test stubs"""

    def test_create_model(self):
        """Test case for create_model

        
        """
        response = self.client.open(
            '//models',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_version(self):
        """Test case for create_version

        
        """
        response = self.client.open(
            '//models/{type}/versions'.format(type='type_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_model(self):
        """Test case for update_model

        Query to search multiple objects
        """
        response = self.client.open(
            '//models/{type}/versions/{versionId}'.format(type='type_example', versionId='versionId_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
