from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid input'}
    # Escape or validate host to prevent injection
    host = subprocess.quote(host)
    return {'status': 'completed', 'output': safe_ping(host)}