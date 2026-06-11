from fastapi import FastAPI
import shlex
import subprocess
def safe_ping(host: str):
    try:
        subprocess.run(['ping', '-c', '1', shlex.quote(host)], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)