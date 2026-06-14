from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        if host.startswith(('192.168.', '172.16.', '10.')) or host == 'localhost':
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        else:
            return {'status': 'failed', 'error': 'Invalid host'}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}