from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with proper sanitization
    safe_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}