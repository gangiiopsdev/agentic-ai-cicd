from fastapi import FastAPI
import subprocess
import re
import asyncio

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in '.-')

async def safe_ping(host: str):
    # Ensure the host is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}

    sanitized_host = subprocess.quote(sanitize_input(host))  # Safely handle user inputs with sanitization
    try:
        result = await asyncio.create_subprocess_exec('ping', sanitized_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = await result.communicate()
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}