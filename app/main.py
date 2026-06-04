from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize and quote input to prevent command injection
    sanitized_host = shlex.quote(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}