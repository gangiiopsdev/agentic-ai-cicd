from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    if not host.isalnum():
        return {'error': 'Invalid host'}
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)