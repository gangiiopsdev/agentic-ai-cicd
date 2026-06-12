from fastapi import FastAPI
import subprocess
def run_ping(host: str):    try:
        # Secure implementation using subprocess.run
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return run_ping(host)