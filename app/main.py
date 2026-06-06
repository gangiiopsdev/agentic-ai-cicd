from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize user input to prevent command injection
    safe_host = host.strip()
    if safe_host and not any(char in safe_host for char in "<>{}\"'":
        args = shlex.split(f'ping {safe_host}')
        subprocess.call(args)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host input'}, 400