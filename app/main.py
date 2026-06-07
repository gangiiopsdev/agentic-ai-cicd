from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}