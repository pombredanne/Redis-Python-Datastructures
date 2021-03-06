"""
This is module contains RedisDict, which allows users to interact with
Redis strings using the standard Python dictionary syntax.
"""
import UserDict
import redis
import redis_config

class RedisDict(UserDict.DictMixin):
    def __init__(self, redis_client=redis_config.CLIENT):
        """
        Parameters:
        - redis_client: configured redis_client to use for all requests.
                        should be fine to monkey patch this to set the
                        default settings for your environment...
        """
        self._client = redis_client

    def keys(self, pattern="*"):
        return self._client.keys(pattern)

    def __len__(self):
        return self._client.dbsize()

    def __getitem__(self, key):
        return self._client.get(key)

    def __setitem__(self, key, val):
        return self._client.set(key, val)

    def __delitem__(self, key):
        return self._client.delete(key)

    def __contains__(self, key):
        return self._client.exists(key)

    def get(self, key, default=None):
        return self.__getitem__(key) or default

