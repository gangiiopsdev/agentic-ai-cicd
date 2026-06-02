from fastapi import FastAPI
import os
import shlex
import asyncio

class SafePing:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        try:
            command = ['ping', '-c', '1', host]
            result = await asyncio.to_thread(os.system, command)
            return {'status': 'Ping successful'}
        except Exception as e:
            return {'status': f'Ping failed: {e}'}

safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    if not all(c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_" for c in host):
        return {'status': 'Invalid host'}
    return safe_ping_instance.ping(host)