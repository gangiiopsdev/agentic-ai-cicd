from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if host.strip() and not any(char in host for char in [';', '&', '|', '`']):
        return run_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid input'}