from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Escape the host parameter to prevent command injection
    escaped_host = shlex.quote(host)
    try:
        output = subprocess.check_output(['ping', '-c', '4', escaped_host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or len(host.split('.')) != 4:
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)