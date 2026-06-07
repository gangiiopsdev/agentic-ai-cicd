from fastapi import FastAPI
import subprocess
import shlex
import asyncio

global app = FastAPI()

async def safe_ping(host):
    args = ['ping', '-c', '1'] + shlex.split(host)  # Use shlex to safely split the host input
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    return result.stdout

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    output = safe_ping(host)  # Remove the async keyword to avoid confusion
    return {'status': 'completed', 'output': output}