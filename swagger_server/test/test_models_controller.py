# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.push_to_redis import PushToRedis
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestModelsController(BaseTestCase):
    """ ModelsController integration test stubs """

    def test_update_model(self):
        """
        Test case for update_model

        
        """
        response = self.client.open('//models',
                                    method='POST')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_model_of_detect(self):
        """
        Test case for update_model_of_detect

        Query to search multiple objects
        """
        response = self.client.open('//models/detect/{versionId}'.format(versionId='versionId_example'),
                                    method='POST')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_model_of_feature(self):
        """
        Test case for update_model_of_feature

        Query to search multiple objects
        """
        response = self.client.open('//models/feature/{versionId}'.format(versionId='versionId_example'),
                                    method='POST')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
