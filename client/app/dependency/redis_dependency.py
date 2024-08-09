import aioredis


async def get_redis_blocked_token():
    redis = aioredis.from_url("redis://localhost:6379/1")
    try:
        yield redis
    except Exception as e:
        raise e
    finally:
        await redis.close()
