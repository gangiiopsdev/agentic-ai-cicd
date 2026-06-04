from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.strip().endswith('.localdomain.com'):
        return False
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return result.returncode == 0
    except Exception as e:
        print(f'Error pinging {host}: {e})
        return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'message': 'Invalid host'}