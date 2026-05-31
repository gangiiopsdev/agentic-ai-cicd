from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input to prevent injection attacks
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host name')
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    # Use the safe function
    return {'status': 'completed', 'output': safe_ping(host)}