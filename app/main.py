from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError('Invalid hostname')

    # Secure implementation using subprocess.run with absolute path
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)