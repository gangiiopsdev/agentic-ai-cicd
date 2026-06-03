from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        pass

    @staticmethod
def safe_ping(host: str):
        try:
            # Sanitize the input by using parameterized command
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_pinger = SafePing()
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 50:
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_pinger.safe_ping(host)