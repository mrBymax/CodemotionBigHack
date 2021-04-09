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
    return [
  {
    "found": True,
    "class": "Mouse",
    "imgEndpoint": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group0/2e/a5/77/2f/ba/2c/41/ea/mobile_pos_image/files/mobile_pos.jpg/_jcr_content/translations/en.mobile_pos.jpg",
    "score": 0.96
  }
]


def classify_text(body):  # noqa: E501
    """Classify the text

     # noqa: E501

    :param body: Conversation
    :type body: list | bytes

    :rtype: List[ItemClassification]
    """
    if connexion.request.is_json:
        body = [ConversationObject.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return [
  {
    "question": "Does ST produce mices?",
    "answer": {
      "response": "Yes, we produce mices",
      "items": [
        {
          "found": True,
          "class": "Mouse",
          "imgEndpoint": "https://www.st.com/content/ccc/fragment/application_related/end_app_information/end_app_block_diagram/group0/2e/a5/77/2f/ba/2c/41/ea/mobile_pos_image/files/mobile_pos.jpg/_jcr_content/translations/en.mobile_pos.jpg",
          "score": 0.96
        }
      ]
    }
  }
]


def get_info(itemName):  # noqa: E501
    """Get info about the object

     # noqa: E501

    :param itemName: The unique name of the item
    :type itemName: str

    :rtype: List[ItemComponent]
    """
    return [
  {
    "componentName": "BALF-NRG-02D3",
    "description": "Programmable Bluetooth&reg; LE 5.2 Wireless SoC"
  }
]
