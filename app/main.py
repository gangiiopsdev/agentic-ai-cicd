from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not all(c.isalnum() or c in '.-+' for c in host):
        return {'error': 'Invalid hostname'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}