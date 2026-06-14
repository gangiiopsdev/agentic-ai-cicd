from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def secure_ping(host):
    args = ['ping', shlex.quote(host)]
    await asyncio.create_subprocess_exec(*args, check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    await secure_ping(host)
    return {'status': 'completed'}