from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = host.strip()
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        # Use a fixed path for the executable to mitigate risks
        result = subprocess.run(['/usr/bin/ping', '-c', '1', sanitized_host], capture_output=True, text=True)
        if result.returncode == 0:
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'error', 'message': 'Ping failed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

# Add input validation and error handling for better security