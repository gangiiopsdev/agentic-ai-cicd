from fastapi import FastAPI
import subprocess
from shlex import quote
import os

def sanitize_input(user_input):
    return ''.join(filter(str.isalnum, user_input))

async def run_safe_command(command_parts):
    safe_command = [os.path.abspath(cmd) for cmd in command_parts]
    result = await asyncio.create_subprocess_exec(*safe_command, check=True)
    output, _ = await result.communicate()
    return output.decode().strip()

class SafePing:
    def __init__(self):
        self.ping_path = os.path.abspath('ping')

    async def ping_host(self, host: str):
        sanitized_host = quote(sanitize_input(host))
        return await run_safe_command([self.ping_path, '-c', '1', sanitized_host])

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing()
    result = await safe_ping.ping_host(host)
    return {'status': 'completed', 'result': result}