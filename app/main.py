from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return None, 'Invalid host'
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout, None

@app.get("/ping")
def ping(host: str):
    stdout, error = safe_ping(host)
    if error:
        return {'status': 'error', 'output': error}
    return {'status': 'completed', 'output': stdout}