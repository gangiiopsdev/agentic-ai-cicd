from fastapi import FastAPI
import subprocess
import asyncio

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    await asyncio.create_subprocess_exec('ping', host)

def ping_route(host: str):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        result = loop.run_until_complete(ping(host))
        return {'result': 'Pong'}
    finally:
        loop.close()