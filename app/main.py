from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 255

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}

    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}