from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Use a whitelist for allowed hosts or validate input more strictly
        if not host.strip().endswith('allowed_domain.com'):
            raise ValueError('Invalid host')
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return ping(host)