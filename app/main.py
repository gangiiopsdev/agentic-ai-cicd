from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping/")
def ping(host: str):
    # Validate host input
    if not host.isalnum() or len(host) > 255:
        return {'error': 'Invalid hostname'}

    # Sanitize host input to prevent shell injection
    safe_host = subprocess.quote(host)
    args = ['ping', safe_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}