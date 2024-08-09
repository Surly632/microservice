import aioredis


async def get_redis_blocked_token():
    redis = aioredis.from_url("redis://redis:6379/1")
    try:
        yield redis
    except Exception as e:
        raise e
    finally:
        await redis.close()


async def get_redis_open_orders():
    redis = aioredis.from_url("redis://redis:6379/1")
    try:
        yield redis
    except Exception as e:
        raise e
    finally:
        await redis.close()
