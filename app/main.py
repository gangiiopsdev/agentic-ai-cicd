from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Ensure the host does not contain harmful characters or commands
    if '&&' in host or '|' in host or ';' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], check=True, shell=False, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e), 'output': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)