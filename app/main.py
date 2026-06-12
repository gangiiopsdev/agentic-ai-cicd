from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host or host.strip() == '':
        return 'Invalid host'
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    return {'status': 'completed', 'output': safe_ping(host)}