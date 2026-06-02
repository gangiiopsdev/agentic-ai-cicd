from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid input'}
    result = subprocess.run(['ping', host], shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}