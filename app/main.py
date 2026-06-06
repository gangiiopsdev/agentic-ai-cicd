from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate the host to ensure it's a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host')
        subprocess.run(['ping', '-c', '1', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return result