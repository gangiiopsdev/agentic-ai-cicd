from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host:
        return False
    # Safe implementation using check_output
    try:
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.output.decode()}')
        return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}