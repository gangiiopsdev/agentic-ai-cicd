from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    try:
        # Use safe method to avoid shell injection
        subprocess.run(['ping', host], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid input'}
    result = ping_safe(host)
    return result