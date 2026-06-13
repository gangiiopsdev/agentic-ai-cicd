from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate and sanitize host input
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)