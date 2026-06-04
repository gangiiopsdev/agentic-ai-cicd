from fastapi import FastAPI
import subprocess

app = FastAPI()

global_result = None

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host parameter
    if not host or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        global_result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': global_result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}