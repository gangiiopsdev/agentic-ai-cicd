from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    # Implement your validation logic here
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', '--'] + [host]
    process = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': process.stdout, 'error': process.stderr}