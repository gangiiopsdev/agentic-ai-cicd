from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        subprocess.run(['ping', *shlex.split(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it does not contain malicious content
    if any(char in host for char in ['&&', ';', '|', '`']):
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)