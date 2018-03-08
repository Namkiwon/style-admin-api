import connexion
from swagger_server.models.push_to_redis import PushToRedis
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from controller.push import Push

def update_model():
    """
    :rtype: None
    """
    return 'do some magic!'


def update_model_of_detect(versionId):
    """
    Query to search multiple objects
    update model of service with model&#39;s versionId
    :param versionId: model&#39;s version
    :type versionId: str

    :rtype: PushToRedis
    """
    return Push.update_model_of_detect(versionId)


def update_model_of_feature(versionId):
    """
    Query to search multiple objects
    update model of service with model&#39;s versionId
    :param versionId: model&#39;s version
    :type versionId: str

    :rtype: PushToRedis
    """
    return 'do some magic!'
