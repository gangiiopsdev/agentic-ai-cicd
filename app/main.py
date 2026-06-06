from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Ensure the host input is safe to use with ping
        if not host.isalnum():
            raise ValueError('Invalid host input')
        subprocess.call(shlex.split(f"ping {host}"))
    except Exception as e:
        return {'error': str(e)}
    return {'status': 'completed'}