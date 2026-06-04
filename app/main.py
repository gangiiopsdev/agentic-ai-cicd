from fastapi import FastAPI
import subprocess
import shlex
gimport os

app = FastAPI()

async def is_valid_host(host: str) -> bool:
    return all(c.isalnum() or c in '.-' for c in host)

def sanitize_input(user_input):
    safe_input = ''.join(e if e.isalnum() or e in '-.' else 'A' for e in user_input)
    return shlex.quote(safe_input)

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid input detected in host parameter')
    args = ['ping', sanitize_input(host)]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}