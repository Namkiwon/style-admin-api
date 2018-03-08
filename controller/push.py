import redis
import os

REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
rconn = redis.StrictRedis(REDIS_SERVER, port=6379, password=REDIS_PASSWORD)
options = {
  'REDIS_SERVER': REDIS_SERVER,
  'REDIS_PASSWORD': REDIS_PASSWORD
}


class Push:
    @staticmethod
    def update_model_of_detect(versionId):
        # print(REDIS_SERVER)
        id = rconn.lpush('originman','hi')
        return str(id)