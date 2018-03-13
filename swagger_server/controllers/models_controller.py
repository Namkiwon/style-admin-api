import connexion
import six

from swagger_server.models.update_model_response import UpdateModelResponse  # noqa: E501
from swagger_server import util
from controller.models import Model


def create_model():  # noqa: E501
    """

    create model # noqa: E501


    :rtype: None
    """
    return Model.create_model()


def create_version(type):  # noqa: E501
    """

    create version # noqa: E501

    :param type: type of model
    :type type: str

    :rtype: None
    """
    return Model.create_version(type)


def update_model(type, versionId):  # noqa: E501
    """Query to search multiple objects

    update model of service with model&#39;s versionId # noqa: E501

    :param type: model&#39;s type
    :type type: str
    :param versionId: model&#39;s version
    :type versionId: str

    :rtype: UpdateModelResponse
    """
    return Model.update_model(type,versionId)
