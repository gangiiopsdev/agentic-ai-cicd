from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode(), 'error': result.stderr.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_wrapper(host: str):
    # Validate input for safety
    if host and len(host) <= 100 and all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return ping(host)
    else:
        return {'status': 'error', 'message': 'Invalid input'}