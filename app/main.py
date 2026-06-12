from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host parameter'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = subprocess.run(['ping', '-c', '1', safe_ping(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}