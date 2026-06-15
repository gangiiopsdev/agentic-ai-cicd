from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', '--', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}
app = FastAPI()
@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)