from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid hostname'}
    result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}