from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)