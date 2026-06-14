from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not isinstance(host, str) or len(host.strip()) == 0:
        return "Invalid host"
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)