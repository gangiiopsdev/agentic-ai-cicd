from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():  # Basic validation of host
        return 'Invalid host'
    args = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}