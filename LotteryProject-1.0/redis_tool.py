#缓存操作
import redis
class redis_tool():
    redisInstance = None
    def __init__(self) -> None:
        self.connectionRedis()
    #创建链接   
    def connectionRedis(self):
        pool = redis.ConnectionPool(host='167.179.103.34', port=6379, decode_responses=True)
        self.redisInstance = redis.Redis(connection_pool=pool)
    #缓存字符串类型的值
    def setValue(self,k,v):
        self.redisInstance.set(k,v)
    #获取字符串类型的值
    def getValue(self,k):
        return self.redisInstance.get(k)
    #缓存集合类型的值    
    def setListValue(self,k,v):
        vS = [str(x) for x in v]
        vS2 = ','.join(vS)
        self.setValue(k,vS2)
    #获取集合类型的值    
    def getListValue(self,k):
        value =  self.getValue(k)
        if value == None:
            return None  
        return list(map(int,value.split(',')))