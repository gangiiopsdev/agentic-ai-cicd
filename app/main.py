from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host.strip():
        return {'status': 'error', 'result': 'Host parameter is empty'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}