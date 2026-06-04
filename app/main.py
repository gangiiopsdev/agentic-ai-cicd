from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    safe_host = ''.join(e for e in host if e.isalnum() or e in '._-')
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}