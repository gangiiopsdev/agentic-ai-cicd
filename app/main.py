from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    safe_ping = SafePing()
    # Ensure host input is a valid IP address or hostname
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": 'failed', 'error': 'Invalid host input'}
    sanitized_host = subprocess.escape(host)
    return safe_ping.ping(sanitized_host)