from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}

@app.get("/ping")
def ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}