from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Sanitize the input to prevent command injection
    host = shlex.quote(host)
    try:
        subprocess.run(['ping', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)