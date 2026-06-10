from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Validate input to only allow alphanumeric characters and common delimiters
        return {'status': 'error', 'result': 'Invalid host'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}