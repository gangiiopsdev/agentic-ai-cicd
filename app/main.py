from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize and quote the input to prevent command injection
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True)
    return {'status': 'completed'}