from fastapi import FastAPI
import os
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname')
        args = ['ping', '-c', '1', host]
        subprocess.run(args, check=True)
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return {'status': 'completed'}