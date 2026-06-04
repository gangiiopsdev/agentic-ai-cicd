from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with absolute path and argument handling
    result = subprocess.run(['/usr/bin/ping', '-c 1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}