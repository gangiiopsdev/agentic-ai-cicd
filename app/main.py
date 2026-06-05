from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input here (e.g., allow only specific domains)
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}