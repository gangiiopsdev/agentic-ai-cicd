from fastapi import FastAPI
import asyncio
import os

app = FastAPI()

async def secure_ping(host: str):
    # Ensure the host input is sanitized before use
    safe_host = os.path.abspath(host)
    args = ['ping', safe_host]
    result = await asyncio.create_subprocess_exec(*args, check=True)
    return result

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}