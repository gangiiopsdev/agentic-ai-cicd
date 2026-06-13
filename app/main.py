from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if 'ping' not in host.split():
        return False
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, bool) and not result:
        return {'error': 'Invalid host'}, 400
    return {'status': 'completed', 'result': result}