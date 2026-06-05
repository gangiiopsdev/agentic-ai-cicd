from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        response = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': response.stdout.decode(), 'stderr': response.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.replace('.', '').isdigit() and len(host) > 15:
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)