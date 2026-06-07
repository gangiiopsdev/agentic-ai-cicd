from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize user input to prevent command injection
    safe_host = host.strip()
    if safe_host and not any(char in safe_host for char in "<>{}\"'"):
        try:
            args = shlex.split(f'ping {safe_host}')
            subprocess.call(args)
            return {'status': 'completed'}
        except Exception as e:
            return {'error': str(e)}, 500
    else:
        return {'error': 'Invalid host input'}, 400