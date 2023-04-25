""" Cronjob python script to capture leaderboard at specified time on cron. """

import asyncio

import redis
import time

from cmyui.mysql import AsyncSQLPool
from dotenv import dotenv_values


async def main():
    env = dict(dotenv_values('.env'))

    redis_server = redis.StrictRedis()
    capture_time = round(time.time())

    for leaderboard in redis_server.scan_iter("bancho:leaderboard:[0-9]"):
        mode = leaderboard.decode().split(':')[-1]

        leaderboard_values = redis_server.zrange(leaderboard.decode(), 0, -1, withscores=True)

        # Sort players by PP count.
        leaderboard_values = sorted(
            leaderboard_values,
            key=lambda _: _[1],
            reverse=True
        )

        # Prepare values to insert in database.
        values = ', '.join([
            f'({player[0].decode()}, {mode}, {rank + 1}, {capture_time})'
            for rank, player in enumerate(leaderboard_values)
        ])

        connection = AsyncSQLPool()
        await connection.connect({
            'user': env['DB_USER'],
            'password': env['DB_PASS'],
            'host': env['DB_HOST'],
            'db': env['DB_NAME'],
        })

        # @TODO Maybe this will break smth cuz there might be to many values to insert by one iteration.
        await connection.execute(
            'INSERT INTO leaderboard_history '
            '(uid, mode, player_rank, capture_time) VALUES '
            f'{values}'
        )

asyncio.run(main())
