from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using a fixed command list
    safe_command = ['ping', 'example.com']
    subprocess.run(safe_command, check=True, capture_output=True)
    return {'status': 'completed'}