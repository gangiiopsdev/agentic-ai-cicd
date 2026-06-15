from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

async def safe_ping(host: str):
    try:
        output = await subprocess.check_output(['ping', quote(host)], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output}'

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed', 'output': await safe_ping(host)}

def validate_host(host: str) -> bool:
    # Enhanced validation to prevent command injection attacks
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars or char == '@' or char == '&' or char == ';' or char == '$' or char == '>' or char == '<' or char == '|':
            return False
    return True