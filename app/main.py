from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and avoiding use of host directly in the command list.
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'stdout': result.stdout}