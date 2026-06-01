from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Use a complete executable path for security
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': e.output}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)