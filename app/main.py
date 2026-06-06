from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'response': 'Invalid host'}
    response = run_ping(host)
    return {'status': 'completed', 'response': response}

def is_valid_host(host: str) -> bool:
    # Add validation logic for the host here
    return True