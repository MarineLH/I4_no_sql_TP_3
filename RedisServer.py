import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""

hash_name = "Notes"


def get_note(id):
    try:
        r = connection_redis_server()
        return r.hget(hash_name, id)
    except Exception as e:
        print(e)


def post_note(id, msg):
    try:
        r = connection_redis_server()
        return r.hset(hash_name, id, msg)
    except Exception as e:
        print(e)


def get_all_notes():
    try:
        r = connection_redis_server()
        return r.hgetall(hash_name)
    except Exception as e:
        print(e)


def delete_note(id):
    try:
        r = connection_redis_server()
        return r.hdel(hash_name, id)
    except Exception as e:
        print(e)


def connection_redis_server():
    try:
        return redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    except Exception as e:
        return e
