from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', '--', host], capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        return False
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if host.isdigit() and len(host) <= 4:
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}