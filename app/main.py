from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    cmd = ['ping', host]
    result = subprocess.run(cmd, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}