from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate the host input to prevent command injection
    if not host or len(host) > 255:
        raise ValueError('Invalid host input')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        return {'status': 'completed', 'output': safe_ping(host)}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}