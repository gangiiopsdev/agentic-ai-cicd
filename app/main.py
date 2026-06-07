from fastapi import FastAPI
import re
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Use shlex.quote to safely escape command arguments
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid host"}
    # Add additional validation for security
    import socket
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        return {"status": "failed", "error": "Invalid host address"}
    return safe_ping(host)