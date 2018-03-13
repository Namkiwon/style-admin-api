import redis
import os

#interpreter Environment에서 변수들을 가져온다
REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
rconn = redis.StrictRedis(REDIS_SERVER, port=6379, password=REDIS_PASSWORD)

options = {
  'REDIS_SERVER': REDIS_SERVER,
  'REDIS_PASSWORD': REDIS_PASSWORD
}

class Model:
    @staticmethod
    def update_model(type,versionId):
        # print(REDIS_SERVER)
        try:
            id = rconn.lpush('originman',versionId)
        except Exception as e:
            print(e)
        return str(id)

    @staticmethod
    def create_model():
        print('create model');

    @staticmethod
    def create_version(type):
        print('create version of '+type+'model');