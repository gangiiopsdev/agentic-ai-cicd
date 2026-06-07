from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'invalid_host', 'message': 'Invalid host provided'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    return ping(host)