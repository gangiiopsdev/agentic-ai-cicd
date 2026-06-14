from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if host.isprintable() and all(c not in host for c in '\n\r\t'):  # Check for printable characters and no special control characters
        subprocess.call(['ping', host])
    else:
        return {'error': 'Invalid input'}

    return {'status': 'completed'}