from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.Popen without shell=True and validate input
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=400, detail='Invalid host name')
    safe_ping(host)
    return {'status': 'completed'}

# Helper function to validate the host input
def validate_host(host):
    # Basic validation: check for disallowed characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in host)