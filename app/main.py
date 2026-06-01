from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    # Implement a simple check for safe hostname characters
    return all(char.isalnum() or char in ('.', '-') for char in hostname)

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}