import connexion
import six

from swagger_server.models.conversation_object import ConversationObject  # noqa: E501
from swagger_server.models.img_file import IMGFile  # noqa: E501
from swagger_server.models.item_classification import ItemClassification  # noqa: E501
from swagger_server.models.item_component import ItemComponent  # noqa: E501
from swagger_server import util


def classify_image(body):  # noqa: E501
    """Classify the image

     # noqa: E501

    :param body: Base64 image
    :type body: dict | bytes

    :rtype: List[ItemClassification]
    """
    if connexion.request.is_json:
        body = IMGFile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def classify_text(body):  # noqa: E501
    """Classify the text

     # noqa: E501

    :param body: Conversation
    :type body: list | bytes

    :rtype: List[ItemClassification]
    """
    if connexion.request.is_json:
        body = [ConversationObject.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def get_info(itemName):  # noqa: E501
    """Get info about the object

     # noqa: E501

    :param itemName: The unique name of the item
    :type itemName: str

    :rtype: List[ItemComponent]
    """
    return 'do some magic!'
