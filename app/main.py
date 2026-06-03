from fastapi import FastAPI
import os
import shlex
import asyncio
import subprocess

class SafePing:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        try:
            command = ['ping', '-c', '1', shlex.quote(host)]
            result = await asyncio.to_thread(subprocess.run, command, capture_output=True, text=True)
            return {'status': 'Ping successful', 'output': result.stdout}
        except Exception as e:
            return {'status': f'Ping failed: {e}'}
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    if not all(c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_" for c in host) or ' ' in host:
        return {'status': 'Invalid host'}
    return safe_ping_instance.ping(host)