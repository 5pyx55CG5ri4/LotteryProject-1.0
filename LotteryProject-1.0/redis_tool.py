#缓存操作
import redis
class redis_tool():
    redisInstance = None
    def __init__(self) -> None:
        self.connectionRedis()
    def connectionRedis(self):
        pool = redis.ConnectionPool(host='167.179.103.34', port=6379, decode_responses=True)
        self.redisInstance = redis.Redis(connection_pool=pool)
    def setValue(self,k,v):
        self.redisInstance.set(k,v)
    def getValue(self,k):
        return self.redisInstance.get(k)
    def setListValue(self,k,v):
        vS = [str(x) for x in v]
        vS2 = ','.join(vS)
        self.setValue(k,vS2)
    def getListValue(self,k):
        value =  self.getValue(k)
        if value == None:
            return None  
        return list(map(int,value.split(',')))