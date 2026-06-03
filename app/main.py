from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.isdigit():
        try:
            output = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except subprocess.CalledProcessError:
            return False
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        return {'status': 'completed' if safe_ping(host) else 'failed'}
    except ValueError as e:
        return {'error': str(e)}, 400