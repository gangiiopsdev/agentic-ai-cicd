from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add validation logic for the host parameter
    return all(c.isalnum() or c in '.:-' for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}