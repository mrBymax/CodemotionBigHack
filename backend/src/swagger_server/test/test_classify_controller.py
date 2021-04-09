# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.conversation_object import ConversationObject  # noqa: E501
from swagger_server.models.img_file import IMGFile  # noqa: E501
from swagger_server.models.item_classification import ItemClassification  # noqa: E501
from swagger_server.models.item_component import ItemComponent  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClassifyController(BaseTestCase):
    """ClassifyController integration test stubs"""

    def test_classify_image(self):
        """Test case for classify_image

        Classify the image
        """
        body = IMGFile()
        response = self.client.open(
            '/v1/classify/classifyImage',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_classify_text(self):
        """Test case for classify_text

        Classify the text
        """
        body = [ConversationObject()]
        response = self.client.open(
            '/v1/classify/classifyText',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_info(self):
        """Test case for get_info

        Get info about the object
        """
        response = self.client.open(
            '/v1/classify/getInfo/{itemName}'.format(itemName='itemName_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
