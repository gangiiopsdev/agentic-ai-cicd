from fastapi import FastAPI
import subprocess

class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            # Sanitize the host input to prevent injection attacks
            host = subprocess.list2cmdline([host])
            result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() and not '.' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    return SafePing.safe_ping(host)