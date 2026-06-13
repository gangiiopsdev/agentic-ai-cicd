from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    if '@' in host or ';' in host or '&' in host or '|' in host or '`' in host or '$' in host:
        return {'status': 'invalid', 'message': 'Potential injection detected'}
    return safe_ping(host)