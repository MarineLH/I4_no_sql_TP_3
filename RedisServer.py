import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""


def get_note(id):
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        return r.hget("Notes", id)
    except Exception as e:
        print(e)


def post_note(id, msg):
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        return r.hset("Notes", id, msg)
    except Exception as e:
        print(e)


def get_all_notes():
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        return r.hgetall("Notes")
    except Exception as e:
        print(e)


def delete_note(id):
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        return r.hdel("Notes", id)
    except Exception as e:
        print(e)
