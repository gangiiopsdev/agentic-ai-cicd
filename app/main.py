from fastapi import FastAPI
import re
import subprocess
class PingCommand:
    @staticmethod
def run(host: str):
        try:
            # Sanitize the input to prevent command injection
            safe_host = subprocess.quote(host)
            result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9._%-]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    safe_host = subprocess.quote(host)
    return PingCommand.run(safe_host)