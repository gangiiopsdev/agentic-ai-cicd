from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
global app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid input'}
    return {'status': 'completed', 'output': safe_ping(host)}