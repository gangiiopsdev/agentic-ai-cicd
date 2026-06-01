from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {'status': 'failed', 'error': 'Invalid host name'}
    return safe_ping(host)