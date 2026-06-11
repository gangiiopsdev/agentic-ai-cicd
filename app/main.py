from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Safe implementation using check_output to prevent shell injection
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': result.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e.output)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)