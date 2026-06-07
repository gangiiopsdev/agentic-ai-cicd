from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed for {host}: {e.stderr.decode()}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'message': 'Ping failed'}