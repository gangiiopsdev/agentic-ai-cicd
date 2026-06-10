from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout, result.stderr

@app.get("/ping")
def ping(host: str):
    stdout, stderr = safe_ping(host)
    return {'status': 'completed', 'stdout': stdout, 'stderr': stderr}