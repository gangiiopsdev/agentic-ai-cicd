from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host input to ensure it is a valid IP address or hostname
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def validate_host(host: str) -> bool:
    # Add your validation logic here
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)