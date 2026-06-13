from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it does not contain malicious content
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    return {'status': 'completed', 'output': safe_ping(host)}