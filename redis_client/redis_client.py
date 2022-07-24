from time import time
from proxypool.schemas.proxy import Proxy
from proxypool.storages.storageredis import RedisClient
from proxypool.storages.storagebase import StorageBase

if __name__ == '__main__':
    conn: StorageBase = RedisClient('192.168.2.119', 6000)
    proxy = Proxy("1.1.1.1", 80)
    proxy.set_protol('SOCKS4')
    proxy.set_last_check_time(int(time()))
    proxy.set_score(50)
    proxy.set_global(False)
    print(proxy.dump())
    conn.add(proxy)

    proxx = conn.random()
    print(proxx)

    conn.clean()
