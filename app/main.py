from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if '@' in host or '>' in host or '<' in host or '&' in host:
        raise ValueError('Invalid characters in host name')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)