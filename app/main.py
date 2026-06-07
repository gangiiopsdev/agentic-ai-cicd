from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def run(host: str):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent shell injection
    if not host.isalnum() and not all(c in '-.' for c in host):
        raise ValueError('Invalid hostname')
    return PingCommand.run(host)