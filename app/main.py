from fastapi import FastAPI
import os

class SafePing:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        await asyncio.create_subprocess_exec(*args)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing(host)
    await safe_ping.execute()
    return {'status': 'completed'}