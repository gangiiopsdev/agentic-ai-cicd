from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Use a whitelist of allowed hosts or further validate the input
    if host not in ['127.0.0.1', 'localhost']:  # Example validation
        return {'error': 'Invalid host'}
    try:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)