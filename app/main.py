from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return result