from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'error': 'Invalid host'}

    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)

    if result.returncode != 0:
        return {'status': 'failed', 'output': result.stderr}

    return {'status': 'completed', 'output': result.stdout}