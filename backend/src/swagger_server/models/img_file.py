# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class IMGFile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, image_b64: str=None):  # noqa: E501
        """IMGFile - a model defined in Swagger

        :param image_b64: The image_b64 of this IMGFile.  # noqa: E501
        :type image_b64: str
        """
        self.swagger_types = {
            'image_b64': str
        }

        self.attribute_map = {
            'image_b64': 'image_b64'
        }

        self._image_b64 = image_b64

    @classmethod
    def from_dict(cls, dikt) -> 'IMGFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IMGFile of this IMGFile.  # noqa: E501
        :rtype: IMGFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image_b64(self) -> str:
        """Gets the image_b64 of this IMGFile.


        :return: The image_b64 of this IMGFile.
        :rtype: str
        """
        return self._image_b64

    @image_b64.setter
    def image_b64(self, image_b64: str):
        """Sets the image_b64 of this IMGFile.


        :param image_b64: The image_b64 of this IMGFile.
        :type image_b64: str
        """

        self._image_b64 = image_b64