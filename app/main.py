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
    if not host.isnumeric() or not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return run_ping(host)

def validate_host(host: str) -> bool:
    # Add logic to validate the host here, e.g., check against a whitelist of allowed hosts
    return True