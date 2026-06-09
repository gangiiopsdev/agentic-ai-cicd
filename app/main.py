from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using subprocess.run with shell=False and list of arguments for security
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {'status': 'error', 'response': 'Invalid host'}
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}